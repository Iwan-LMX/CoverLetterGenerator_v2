#!/usr/bin/env python3
"""PDF generation tool for creating PDF documents from text content"""

try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib.colors import black
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False

import os
from typing import Optional

class PDFGeneratorTool:
    """Tool for generating PDF documents from text content"""
    
    def __init__(self):
        self.last_generated_file = ""
        
    def create_pdf_from_text(self, text_content: str, output_file: str, 
                           title: str = "Cover Letter", author: str = "") -> str:
        """Create a PDF document from text content"""
        
        if not REPORTLAB_AVAILABLE:
            return """Error: ReportLab library not installed. 
Please install it with: pip install reportlab
Alternatively, text file has been generated successfully."""
        
        try:
            # Create directory if it doesn't exist
            dir_path = os.path.dirname(output_file)
            if dir_path:
                os.makedirs(dir_path, exist_ok=True)
            
            # Create PDF document
            doc = SimpleDocTemplate(
                output_file,
                pagesize=letter,
                rightMargin=inch,
                leftMargin=inch,
                topMargin=inch,
                bottomMargin=inch
            )
            
            # Get styles
            styles = getSampleStyleSheet()
            
            # Custom styles
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=16,
                spaceAfter=30,
                alignment=1,  # Center alignment
            )
            
            body_style = ParagraphStyle(
                'CustomBody',
                parent=styles['Normal'],
                fontSize=12,
                spaceAfter=12,
                leading=16,
            )
            
            # Build story (content)
            story = []
            
            # Add title if provided
            if title:
                story.append(Paragraph(title, title_style))
                story.append(Spacer(1, 12))
            
            # Split text into paragraphs and add to story
            paragraphs = text_content.split('\n\n')
            
            for para_text in paragraphs:
                if para_text.strip():
                    # Clean up the text for PDF
                    clean_text = para_text.strip().replace('\n', ' ')
                    story.append(Paragraph(clean_text, body_style))
                    story.append(Spacer(1, 6))
            
            # Build PDF
            doc.build(story)
            
            self.last_generated_file = output_file
            
            # Verify file was created
            if os.path.exists(output_file):
                file_size = os.path.getsize(output_file)
                return f"PDF successfully created: {output_file} ({file_size} bytes)"
            else:
                return f"Error: PDF file was not created at {output_file}"
                
        except Exception as e:
            return f"Error creating PDF: {str(e)}"
    
    def create_cover_letter_pdf(self, cover_letter_text: str, output_file: str,
                              applicant_name: str = "", position: str = "",
                              company: str = "") -> str:
        """Create a professionally formatted cover letter PDF"""
        
        if not REPORTLAB_AVAILABLE:
            return """Error: ReportLab library not installed. 
Please install it with: pip install reportlab
Text file generation completed successfully."""
        
        try:
            # Create directory if it doesn't exist
            dir_path = os.path.dirname(output_file)
            if dir_path:
                os.makedirs(dir_path, exist_ok=True)
            
            # Create PDF document
            doc = SimpleDocTemplate(
                output_file,
                pagesize=letter,
                rightMargin=inch,
                leftMargin=inch,
                topMargin=inch,
                bottomMargin=inch
            )
            
            # Get and customize styles
            styles = getSampleStyleSheet()
            
            # Header style for applicant info
            header_style = ParagraphStyle(
                'Header',
                parent=styles['Normal'],
                fontSize=11,
                alignment=2,  # Right alignment
                spaceAfter=20,
            )
            
            # Date style
            date_style = ParagraphStyle(
                'Date',
                parent=styles['Normal'],
                fontSize=11,
                spaceAfter=20,
            )
            
            # Body paragraph style
            body_style = ParagraphStyle(
                'Body',
                parent=styles['Normal'],
                fontSize=11,
                leading=16,
                spaceAfter=12,
                alignment=0,  # Left alignment
            )
            
            # Signature style
            signature_style = ParagraphStyle(
                'Signature',
                parent=styles['Normal'],
                fontSize=11,
                spaceAfter=6,
            )
            
            # Build story
            story = []
            
            # Add applicant info header if provided
            # if applicant_name:
            #     story.append(Paragraph(f"<b>{applicant_name}</b>", header_style))
            
            # Add date
            # from datetime import datetime
            # current_date = datetime.now().strftime("%B %d, %Y")
            # story.append(Paragraph(current_date, date_style))
            
            # Process cover letter text
            # Split by paragraphs but preserve structure
            lines = cover_letter_text.split('\n')
            current_paragraph = ""
            
            for line in lines:
                line = line.strip()
                if not line:  # Empty line - end of paragraph
                    if current_paragraph:
                        story.append(Paragraph(current_paragraph, body_style))
                        current_paragraph = ""
                else:
                    if current_paragraph:
                        current_paragraph += " " + line
                    else:
                        current_paragraph = line
            
            # Add last paragraph if exists
            if current_paragraph:
                story.append(Paragraph(current_paragraph, body_style))
            
            # Build PDF
            doc.build(story)
            
            self.last_generated_file = output_file
            
            # Verify file was created
            if os.path.exists(output_file):
                file_size = os.path.getsize(output_file)
                return f"Cover letter PDF successfully created: {output_file} ({file_size} bytes)"
            else:
                return f"Error: PDF file was not created at {output_file}"
                
        except Exception as e:
            return f"Error creating cover letter PDF: {str(e)}"
    
    def text_to_pdf(self, text_file_path: str, pdf_output_path: str = "") -> str:
        """Convert a text file to PDF"""
        
        if not os.path.exists(text_file_path):
            return f"Text file not found: {text_file_path}"
        
        # Generate PDF output path if not provided
        if not pdf_output_path:
            base_name = os.path.splitext(text_file_path)[0]
            pdf_output_path = base_name + ".pdf"
        
        try:
            # Read text file
            with open(text_file_path, 'r', encoding='utf-8') as file:
                text_content = file.read()
            
            # Create PDF
            result = self.create_pdf_from_text(
                text_content=text_content,
                output_file=pdf_output_path,
                title=os.path.basename(text_file_path)
            )
            
            return result
            
        except Exception as e:
            return f"Error converting text to PDF: {str(e)}"
    
    def get_last_generated_file(self) -> str:
        """Get the path of the last generated PDF file"""
        return self.last_generated_file if self.last_generated_file else "No PDF file generated yet"
    
    def check_reportlab_installation(self) -> str:
        """Check if ReportLab is properly installed"""
        if REPORTLAB_AVAILABLE:
            return "ReportLab is installed and ready to use"
        else:
            return """ReportLab is not installed. To enable PDF generation, please run:
pip install reportlab

This will allow you to generate professional PDF cover letters."""