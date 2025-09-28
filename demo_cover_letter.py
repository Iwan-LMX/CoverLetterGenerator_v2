#!/usr/bin/env python3
"""
Demo script showing how to use the cover letter generation tools
"""

from custom_tools import PDFTool, TextFileTool, CoverLetterTool
import os

def demo_cover_letter_generation():
    """Demonstrate the cover letter generation workflow"""
    
    print("🎯 Cover Letter Generation Demo")
    print("=" * 50)
    
    # Initialize tools
    pdf_tool = PDFTool()
    text_tool = TextFileTool()
    cover_letter_tool = CoverLetterTool()
    
    # Sample resume text (since we might not have a PDF)
    sample_resume_text = """
John Doe
Software Developer
Email: john.doe@email.com | Phone: (555) 123-4567

EXPERIENCE
Senior Python Developer | ABC Tech (2020-2023)
- Developed web applications using Python, Django, and React
- Built RESTful APIs serving 1M+ daily requests
- Implemented microservices architecture using Docker and Kubernetes
- Collaborated with Agile teams using Git version control

Full Stack Developer | XYZ Solutions (2018-2020)  
- Created database schemas and optimized SQL queries
- Developed front-end interfaces with React and Node.js
- Deployed applications on AWS cloud infrastructure
- Participated in code reviews and mentored junior developers

EDUCATION
Bachelor of Science in Computer Science | State University (2014-2018)

SKILLS
Programming: Python, JavaScript, SQL, Java
Frameworks: Django, React, Node.js, Flask
Tools: Git, Docker, AWS, PostgreSQL, MongoDB
Methodologies: Agile, Scrum, Test-Driven Development
"""
    
    # Step 1: Test text file reading
    print("📋 Step 1: Reading job description...")
    job_file = "sample_job_description.txt"
    
    if os.path.exists(job_file):
        job_result = text_tool.read_job_description(job_file)
        print("✅ Job description loaded successfully")
        job_text = text_tool.get_last_content()
    else:
        print("❌ Job description file not found, using sample text")
        job_text = "We are looking for a Python developer with React experience..."
    
    # Step 2: Use sample resume text (simulating PDF extraction)
    print("\n📄 Step 2: Using sample resume content...")
    print("✅ Resume content loaded")
    
    # Step 3: Generate cover letter
    print("\n✍️ Step 3: Generating cover letter...")
    
    cover_letter_result = cover_letter_tool.generate_cover_letter(
        resume_text=sample_resume_text,
        job_description=job_text,
        company_name="Tech Innovations Inc.",
        position_title="Software Developer",
        output_file="demo_cover_letter.txt"
    )
    
    print("✅ Cover letter generated!")
    print("\n" + "="*50)
    print("Generated Cover Letter:")
    print("="*50)
    
    # Read and display the generated cover letter
    if os.path.exists("demo_cover_letter.txt"):
        with open("demo_cover_letter.txt", 'r') as f:
            print(f.read())
    else:
        # Extract cover letter from result
        if "Cover letter generated and saved" in cover_letter_result:
            cover_letter_content = cover_letter_result.split(":\n\n", 1)[1]
            print(cover_letter_content)
    
    print("\n✅ Demo completed! Check 'demo_cover_letter.txt' for the output.")

def demo_tool_capabilities():
    """Demo individual tool capabilities"""
    
    print("\n🔧 Tool Capabilities Demo")
    print("=" * 30)
    
    # Text Tool Demo
    print("📝 TextFileTool capabilities:")
    text_tool = TextFileTool()
    print("- read_text_file()")
    print("- read_job_description()")
    print("- get_job_summary()")
    print("- write_text_file()")
    
    # PDF Tool Demo  
    print("\n📄 PDFTool capabilities:")
    pdf_tool = PDFTool()
    print("- extract_resume_text()")
    print("- get_resume_summary()")
    print("- read_pdf_pypdf2() and read_pdf_pymupdf()")
    
    # Cover Letter Tool Demo
    print("\n✍️ CoverLetterTool capabilities:")
    cover_letter_tool = CoverLetterTool()
    print("- generate_cover_letter()")
    print("- create_cover_letter_from_files()")
    print("- get_template() and set_template()")
    
    template = cover_letter_tool.get_template()
    print(f"\n📋 Current template preview:")
    print(template[:200] + "...")

if __name__ == "__main__":
    print("🚀 Cover Letter Tools Demo")
    print("Choose demo mode:")
    print("1. Full cover letter generation demo")
    print("2. Tool capabilities overview")
    print("3. Both")
    
    choice = input("\nEnter choice (1, 2, or 3): ").strip()
    
    if choice == "1":
        demo_cover_letter_generation()
    elif choice == "2":
        demo_tool_capabilities()  
    elif choice == "3":
        demo_tool_capabilities()
        demo_cover_letter_generation()
    else:
        print("Invalid choice, running full demo...")
        demo_cover_letter_generation()