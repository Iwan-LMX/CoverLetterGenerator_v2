#!/usr/bin/env python3
"""Cover Letter Generator Agent using Connectonion"""

from connectonion import Agent
from custom_tools import PDFTool, TextFileTool, CoverLetterTool
import os

# Initialize tools
pdf_tool = PDFTool()
text_tool = TextFileTool()
cover_letter_tool = CoverLetterTool()

# Create agent with all the tools
agent = Agent(
    name="CoverLetterGenerator",
    tools=[pdf_tool, text_tool, cover_letter_tool],
    system_prompt="""You are a professional cover letter generator assistant.
    
    Your capabilities:
    1. Read PDF resume files and extract text content
    2. Read text files containing job descriptions  
    3. Generate personalized cover letters based on resume and job requirements
    4. Save cover letters to text files
    
    Workflow:
    - When asked to create a cover letter, first read the resume PDF
    - Then read the job description text file
    - Extract relevant skills and experience that match the job requirements
    - Generate a professional, personalized cover letter
    - Save the result to a text file
    
    Be helpful, professional, and ensure the cover letters are well-structured and compelling.""",
)

def generate_cover_letter_interactive():
    """Interactive cover letter generation"""
    print("📄 Cover Letter Generator Agent")
    print("=" * 50)
    
    # Get file paths from user
    resume_path = input("Enter the path to your resume PDF file: ").strip().strip('"')
    job_path = input("Enter the path to the job description text file: ").strip().strip('"')
    company_name = input("Enter company name (optional): ").strip()
    position_title = input("Enter position title (optional): ").strip()
    output_path = input("Enter output file path (optional, will auto-generate if empty): ").strip().strip('"')
    
    if not output_path:
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"cover_letter_{timestamp}.txt"
    
    print(f"\n🔄 Processing files...")
    
    # Step 1: Read resume
    print("📄 Reading resume PDF...")
    resume_result = agent.input(f"Extract text from the resume PDF file at {resume_path}")
    print("✅ Resume processed")
    
    # Step 2: Read job description
    print("📋 Reading job description...")
    job_result = agent.input(f"Read the job description from text file at {job_path}")
    print("✅ Job description processed")
    
    # Step 3: Generate cover letter
    print("✍️ Generating cover letter...")
    generation_prompt = f"""Generate a cover letter using the resume and job description you just read.
    Company name: {company_name if company_name else 'Not specified'}
    Position: {position_title if position_title else 'Not specified'}
    Save the cover letter to: {output_path}"""
    
    result = agent.input(generation_prompt)
    print(f"✅ Cover letter generated and saved to: {output_path}")
    print(f"\n📝 Result: {result}")
    
    return output_path

def generate_cover_letter_direct(resume_pdf_path: str, job_txt_path: str, 
                               company_name: str = "", position_title: str = "",
                               output_file: str = ""):
    """Direct cover letter generation with file paths"""
    
    print(f"🔄 Generating cover letter...")
    print(f"📄 Resume: {resume_pdf_path}")
    print(f"📋 Job Description: {job_txt_path}")
    
    # Read resume
    resume_result = agent.input(f"Extract text from resume PDF: {resume_pdf_path}")
    
    # Read job description  
    job_result = agent.input(f"Read job description from: {job_txt_path}")
    
    # Generate cover letter
    if not output_file:
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"cover_letter_{timestamp}.txt"
    
    generation_prompt = f"""Create a cover letter using the resume and job description data you just processed.
    Company: {company_name if company_name else 'the organization'}
    Position: {position_title if position_title else 'the position'}  
    Output file: {output_file}
    
    Make it professional and highlight relevant experience."""
    
    result = agent.input(generation_prompt)
    
    print(f"✅ Cover letter saved to: {output_file}")
    return output_file, result

if __name__ == "__main__":
    # Example usage - you can modify these paths
    print("🎯 Cover Letter Generator")
    print("Choose an option:")
    print("1. Interactive mode (you'll be prompted for file paths)")
    print("2. Quick example with sample files")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "1":
        generate_cover_letter_interactive()
    elif choice == "2":
        # Example with sample file paths - modify these to your actual files
        print("\n📝 Example mode - modify the file paths in the code to use your files")
        
        # Sample paths (modify these)
        sample_resume = "sample_resume.pdf"  # Change to your resume path
        sample_job = "job_description.txt"   # Change to your job description path
        
        if os.path.exists(sample_resume) and os.path.exists(sample_job):
            output_file, result = generate_cover_letter_direct(
                resume_pdf_path=sample_resume,
                job_txt_path=sample_job,
                company_name="Example Company",
                position_title="Software Developer"
            )
            print(f"\n📄 Generated: {output_file}")
        else:
            print(f"❌ Sample files not found. Please create:")
            print(f"   - {sample_resume}")
            print(f"   - {sample_job}")
            print("   Or use interactive mode (option 1)")
    else:
        print("Invalid choice. Running interactive mode...")
        generate_cover_letter_interactive()