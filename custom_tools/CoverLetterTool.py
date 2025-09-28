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
[Your Name]
""".strip()
    
    def generate_cover_letter(self, resume_text: str, job_description: str, 
                            company_name: str = "", position_title: str = "",
                            output_file: str = "") -> str:
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
        
        # Save to file if specified
        if output_file:
            try:
                # Create directory if it doesn't exist
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                
                with open(output_file, 'w', encoding='utf-8') as file:
                    file.write(cover_letter)
                return f"Cover letter generated and saved to {output_file}:\n\n{cover_letter}"
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