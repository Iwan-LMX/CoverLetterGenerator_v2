#!/usr/bin/env python3
"""PDF reading tool for extracting text from PDF files"""

import PyPDF2
import fitz  # PyMuPDF (fallback option)
from typing import Optional
import os

class PDFTool:
    """Tool for reading and extracting text from PDF files"""
    
    def __init__(self):
        self.last_extracted_text = ""
        
    def read_pdf_pypdf2(self, file_path: str) -> str:
        """Read PDF using PyPDF2 library"""
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
                return text.strip()
        except Exception as e:
            return f"Error reading PDF with PyPDF2: {str(e)}"
    
    def read_pdf_pymupdf(self, file_path: str) -> str:
        """Read PDF using PyMuPDF library (fallback)"""
        try:
            doc = fitz.open(file_path)
            text = ""
            for page in doc:
                text += page.get_text() + "\n"
            doc.close()
            return text.strip()
        except Exception as e:
            return f"Error reading PDF with PyMuPDF: {str(e)}"
    
    def extract_resume_text(self, file_path: str) -> str:
        """Extract text from a PDF resume"""
        if not os.path.exists(file_path):
            return f"File not found: {file_path}"
        
        if not file_path.lower().endswith('.pdf'):
            return "File must be a PDF"
        
        # Try PyPDF2 first
        text = self.read_pdf_pypdf2(file_path)
        
        # If PyPDF2 fails or returns empty text, try PyMuPDF
        if "Error reading PDF" in text or len(text.strip()) < 10:
            text = self.read_pdf_pymupdf(file_path)
        
        self.last_extracted_text = text
        return f"Successfully extracted resume text from {file_path}:\n\n{text}"
    
    def get_resume_summary(self, file_path: str) -> str:
        """Get a condensed summary of the resume"""
        full_text = self.extract_resume_text(file_path)
        
        if "Error" in full_text or "File not found" in full_text:
            return full_text
        
        # Return first 1000 characters as summary
        summary = full_text[:1000] + ("..." if len(full_text) > 1000 else "")
        return f"Resume summary from {file_path}:\n\n{summary}"
    
    def get_last_extracted_text(self) -> str:
        """Get the last extracted text"""
        return self.last_extracted_text if self.last_extracted_text else "No text extracted yet"