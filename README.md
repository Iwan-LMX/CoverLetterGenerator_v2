# Cover Letter Generator Agent

An intelligent cover letter generation system built with Connectonion that reads PDF resumes and text job descriptions to create personalized cover letters.

## Features

- **PDF Resume Reading**: Extracts text content from PDF resume files
- **Job Description Processing**: Reads and analyzes job descriptions from text files  
- **Intelligent Matching**: Identifies relevant skills and experience that match job requirements
- **Professional Templates**: Uses customizable cover letter templates
- **Automated Generation**: Creates personalized cover letters with company and position details
- **Dual Format Output**: Saves generated cover letters to both TXT and PDF files
- **Professional PDF Layout**: Creates well-formatted PDF documents with proper styling

## Tools Overview

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

2. If you encounter library issues, install them separately:
```bash
pip install PyPDF2 PyMuPDF reportlab
```

## Usage

### Option 1: Using the Connectonion Agent (Recommended)

```python
from connectonion import Agent
from custom_tools import PDFTool, TextFileTool, CoverLetterTool

# Initialize tools
pdf_tool = PDFTool()
text_tool = TextFileTool() 
cover_letter_tool = CoverLetterTool()

# Create agent
agent = Agent(
    name="CoverLetterGenerator",
    tools=[pdf_tool, text_tool, cover_letter_tool],
    system_prompt="You are a professional cover letter generator..."
)

# Use natural language commands
agent.input("Extract text from my resume at resume.pdf")
agent.input("Read job description from job_posting.txt")  
agent.input("Generate a cover letter for Software Developer at Tech Corp and save to cover_letter.txt")
```

### Option 2: Run the Interactive Script

```bash
python cover_letter_agent.py
```

Follow the prompts to:
1. Provide paths to your resume PDF and job description text file
2. Enter company name and position (optional)
3. Specify output file path (optional)

### Option 3: Direct Tool Usage

```python  
from custom_tools import PDFTool, TextFileTool, CoverLetterTool

# Initialize tools
pdf_tool = PDFTool()
text_tool = TextFileTool()
cover_letter_tool = CoverLetterTool()

# Extract resume text
resume_text = pdf_tool.extract_resume_text("path/to/resume.pdf")

# Read job description  
job_text = text_tool.read_job_description("path/to/job.txt")

# Generate cover letter
result = cover_letter_tool.generate_cover_letter(
    resume_text=pdf_tool.get_last_extracted_text(),
    job_description=text_tool.get_last_content(),
    company_name="Your Target Company",
    position_title="Software Engineer", 
    output_file="my_cover_letter.txt"
)
```

## Demo

Run the demo script to see the tools in action:

```bash
python demo_cover_letter.py
```

This will:
- Demonstrate reading job descriptions
- Show cover letter generation with sample data
- Display tool capabilities
- Create a sample cover letter file

## File Structure

```
agentDemo_Connectonion/
|-- README.md
|-- cover_letter_agent.py
|-- custom_tools/
|
|-- input/
|   `-- job_description.txt
|-- output/
|-- prompts/
|   `-- CLGenerator.md
|-- requirements.txt
|-- resumes/
|   `-- <Your CV>.pdf
`-- venv/
```

## Workflow

1. **Input Files**: Provide a PDF resume and text job description
2. **Text Extraction**: Tools extract and process the content  
3. **Analysis**: System identifies matching skills and relevant experience
4. **Generation**: Creates a personalized cover letter using templates
5. **Output**: Saves the final cover letter to a text file

## Customization

### Custom Templates

Modify the cover letter template:

```python
cover_letter_tool = CoverLetterTool()
custom_template = """
Your custom cover letter template here...
Use {{position}}, {{company}}, {{relevant_experience}} placeholders
"""
cover_letter_tool.set_template(custom_template)
```

### Skill Matching

The system automatically identifies matching skills between your resume and job requirements. You can enhance this by:

- Adding more technical keywords to the matching algorithms
- Customizing the experience extraction logic
- Modifying the template to highlight specific achievements

## Troubleshooting

**PDF Reading Issues**: 
- Ensure PyPDF2 and PyMuPDF are installed
- Try both libraries (tool automatically falls back)
- Check if PDF is text-based (not scanned images)

**File Path Issues**:
- Use absolute paths when possible
- Ensure files exist and are readable
- Check file encoding for text files (tool auto-detects)

**Cover Letter Quality**:
- Provide detailed resume and job description content  
- Include relevant keywords in your resume
- Review and customize the generated output

## Examples

See `demo_cover_letter.py` for working examples and `sample_job_description.txt` for input format reference.

The system works best with:
- Detailed PDF resumes with clear sections
- Complete job descriptions with requirements and responsibilities  
- Specific company names and position titles

## Contributing

This project uses the Connectonion framework for LLM agents. To extend functionality:

1. Add new tools in the `custom_tools/` directory
2. Update `__init__.py` to include new tools
3. Modify agent prompts for new capabilities
4. Test with the demo scripts

## License

This project follows the same license as the Connectonion framework.