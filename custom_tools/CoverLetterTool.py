#!/usr/bin/env python3
"""Cover letter generation tool"""

import os
from datetime import datetime
from typing import Optional

class CoverLetterTool:
    """Tool for generating cover letters based on resume and job description"""
    
    def __init__(self):
        self.cover_letter_template = """
Dear Hiring Manager,

I am writing to express my strong interest in the {{position}} position at {{company}}. With my background and skills that align well with your requirements, I am excited about the opportunity to contribute to your team.

{{relevant_experience}}

I am particularly drawn to this opportunity because {{why_company}}. I believe my experience in {{key_skills}} makes me an ideal candidate for this role.

Thank you for considering my application. I look forward to the opportunity to discuss how my skills and enthusiasm can contribute to {{company}}'s continued success.

Sincerely,
{{Your Name}}
""".strip()
    
    def generate_cover_letter(self, resume_text: str, job_description: str, 
                            company_name: str = "", position_title: str = "",
                            output_file: str = "", generate_pdf: bool = True) -> str:
        """Generate a cover letter based on resume and job description"""
        
        # Extract key information
        company = company_name if company_name else "the organization"
        position = position_title if position_title else "the position"
        
        # Create a basic cover letter
        cover_letter = self.cover_letter_template
        
        # Replace placeholders
        cover_letter = cover_letter.replace("{{position}}", position)
        cover_letter = cover_letter.replace("{{company}}", company)
        
        # Add relevant experience section
        experience_section = self._extract_relevant_experience(resume_text, job_description)
        cover_letter = cover_letter.replace("{{relevant_experience}}", experience_section)
        
        # Add why company section
        why_company = f"it aligns with my career goals and offers the opportunity to apply my skills in {position.lower()}"
        cover_letter = cover_letter.replace("{{why_company}}", why_company)
        
        # Extract key skills
        key_skills = self._extract_key_skills(resume_text, job_description)
        cover_letter = cover_letter.replace("{{key_skills}}", key_skills)
        
        # Extract and replace name
        candidate_name = self._extract_name_from_resume(resume_text)
        cover_letter = cover_letter.replace("{{Your Name}}", candidate_name)
        
        # Save to file if specified
        if output_file:
            try:
                # Create directory if it doesn't exist (only if there's a directory path)
                dir_path = os.path.dirname(output_file)
                if dir_path:  # Only create directory if path is not empty
                    os.makedirs(dir_path, exist_ok=True)
                
                # Save text file
                with open(output_file, 'w', encoding='utf-8') as file:
                    file.write(cover_letter)
                
                result_message = f"Cover letter generated and saved to {output_file}"
                
                # Generate PDF if requested
                if generate_pdf:
                    pdf_file = os.path.splitext(output_file)[0] + ".pdf"
                    try:
                        from .PDFGeneratorTool import PDFGeneratorTool
                        pdf_generator = PDFGeneratorTool()
                        
                        pdf_result = pdf_generator.create_cover_letter_pdf(
                            cover_letter_text=cover_letter,
                            output_file=pdf_file,
                            applicant_name=candidate_name,
                            position=position,
                            company=company
                        )
                        
                        if "successfully created" in pdf_result:
                            result_message += f"\nPDF version saved to {pdf_file}"
                        else:
                            result_message += f"\nPDF generation note: {pdf_result}"
                            
                    except Exception as pdf_error:
                        result_message += f"\nPDF generation failed: {str(pdf_error)}"
                
                return f"{result_message}:\n\n{cover_letter}"
                
            except Exception as e:
                return f"Cover letter generated but failed to save to {output_file}: {str(e)}\n\n{cover_letter}"
        
        return f"Cover letter generated:\n\n{cover_letter}"
    
    def _extract_relevant_experience(self, resume_text: str, job_description: str) -> str:
        """Extract relevant experience from resume that matches job description"""
        # Simple keyword matching approach
        resume_lower = resume_text.lower()
        job_lower = job_description.lower()
        
        # Common technical keywords to look for
        tech_keywords = [
            'python', 'java', 'javascript', 'react', 'node.js', 'sql', 'aws', 'docker',
            'kubernetes', 'git', 'agile', 'scrum', 'api', 'database', 'cloud',
            'machine learning', 'data analysis', 'project management', 'leadership'
        ]
        
        # Find matching keywords
        matching_skills = []
        for keyword in tech_keywords:
            if keyword in job_lower and keyword in resume_lower:
                matching_skills.append(keyword)
        
        if matching_skills:
            skills_text = ", ".join(matching_skills[:5])  # Limit to top 5
            return f"My experience with {skills_text} directly aligns with your requirements. I have successfully applied these technologies in previous roles to deliver high-quality solutions and drive business results."
        else:
            return "My professional background has equipped me with the technical skills and experience that align well with the requirements outlined in your job posting."
    
    def _extract_key_skills(self, resume_text: str, job_description: str) -> str:
        """Extract key skills that appear in both resume and job description"""
        resume_lower = resume_text.lower()
        job_lower = job_description.lower()
        
        # Look for common skill patterns
        skills = []
        
        # Programming languages
        prog_langs = ['python', 'java', 'javascript', 'c++', 'c#', 'go', 'rust', 'php']
        for lang in prog_langs:
            if lang in job_lower and lang in resume_lower:
                skills.append(lang.title())
        
        # Technologies and frameworks
        techs = ['react', 'angular', 'vue', 'node.js', 'django', 'flask', 'spring', 'aws', 'azure', 'gcp']
        for tech in techs:
            if tech in job_lower and tech in resume_lower:
                skills.append(tech)
        
        if skills:
            return ", ".join(skills[:3])  # Limit to top 3
        else:
            return "software development, problem-solving, and team collaboration"
    
    def _extract_name_from_resume(self, resume_text: str) -> str:
        """Extract candidate name from resume text"""
        import re
        
        lines = resume_text.strip().split('\n')
        
        # Common patterns for names in resumes
        name_patterns = [
            # First line is often the name
            r'^([A-Z][a-z]+ [A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)',
            # Name followed by title/profession
            r'^([A-Z][a-z]+ [A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s*[-\n]',
            # Name with middle initial
            r'^([A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+)',
            # Name in "Name:" format
            r'^(?:Name|Full Name):\s*([A-Z][a-z]+ [A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)',
        ]
        
        # Try to find name in first few lines
        for i, line in enumerate(lines[:5]):  # Check first 5 lines
            line = line.strip()
            if not line:
                continue
                
            # Skip common header words
            skip_words = ['resume', 'cv', 'curriculum', 'vitae', 'contact', 'phone', 'email', 'address']
            if any(word in line.lower() for word in skip_words):
                continue
            
            # Try each pattern
            for pattern in name_patterns:
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    name = match.group(1).strip()
                    # Validate it looks like a real name (2-3 words, proper capitalization)
                    words = name.split()
                    if 2 <= len(words) <= 3 and all(word[0].isupper() for word in words):
                        return name
        
        # Fallback: try to find first capitalized words that look like names
        for line in lines[:3]:
            line = line.strip()
            words = line.split()
            if len(words) >= 2:
                # Check if first two words are capitalized and look like names
                if (words[0][0].isupper() and words[1][0].isupper() and 
                    words[0].isalpha() and words[1].isalpha() and
                    len(words[0]) > 1 and len(words[1]) > 1):
                    return f"{words[0]} {words[1]}"
        
        # Last resort: return placeholder
        return "Your Name"
    
    def create_cover_letter_from_files(self, resume_pdf_path: str, job_txt_path: str,
                                     company_name: str = "", position_title: str = "",
                                     output_file: str = "") -> str:
        """Create cover letter from file paths (for use with other tools)"""
        
        if not output_file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"cover_letter_{timestamp}.txt"
        
        return f"""To create a cover letter, I need the resume and job description content first.
Please use these steps:

1. Extract resume text: Use PDF tool to read '{resume_pdf_path}'
2. Read job description: Use text tool to read '{job_txt_path}'  
3. Generate cover letter with the extracted content

Output will be saved to: {output_file}"""

    def get_template(self) -> str:
        """Get the current cover letter template"""
        return f"Current cover letter template:\n\n{self.cover_letter_template}"
    
    def set_template(self, new_template: str) -> str:
        """Set a new cover letter template"""
        self.cover_letter_template = new_template
        return "Cover letter template updated successfully"