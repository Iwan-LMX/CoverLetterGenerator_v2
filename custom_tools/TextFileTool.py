#!/usr/bin/env python3
"""Text file reading tool for job descriptions and other text files"""

import os
from typing import Optional

class TextFileTool:
    """Tool for reading and processing text files"""
    
    def __init__(self):
        self.last_read_content = ""
        
    def read_text_file(self, file_path: str, encoding: str = 'utf-8') -> str:
        """Read content from a text file"""
        if not os.path.exists(file_path):
            return f"File not found: {file_path}"
        
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
            self.last_read_content = content
            return f"Successfully read text file {file_path}:\n\n{content}"
        except UnicodeDecodeError:
            # Try with different encoding if UTF-8 fails
            try:
                with open(file_path, 'r', encoding='latin-1') as file:
                    content = file.read()
                self.last_read_content = content
                return f"Successfully read text file {file_path} (latin-1 encoding):\n\n{content}"
            except Exception as e:
                return f"Error reading file {file_path}: {str(e)}"
        except Exception as e:
            return f"Error reading file {file_path}: {str(e)}"
    
    def read_job_description(self, file_path: str) -> str:
        """Read job description from a text file"""
        content = self.read_text_file(file_path)
        
        if "Error" in content or "File not found" in content:
            return content
        
        return f"Job description loaded from {file_path}:\n\n{self.last_read_content}"
    
    def get_job_summary(self, file_path: str, max_chars: int = 2000) -> str:
        """Get a summary of the job description"""
        content = self.read_job_description(file_path)
        
        if "Error" in content or "File not found" in content:
            return content
        
        summary = self.last_read_content[:max_chars]
        if len(self.last_read_content) > max_chars:
            summary += "..."
        
        return f"Job description summary from {file_path}:\n\n{summary}"
    
    def write_text_file(self, file_path: str, content: str, encoding: str = 'utf-8') -> str:
        """Write content to a text file"""
        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            with open(file_path, 'w', encoding=encoding) as file:
                file.write(content)
            return f"Successfully wrote content to {file_path}"
        except Exception as e:
            return f"Error writing to file {file_path}: {str(e)}"
    
    def get_last_content(self) -> str:
        """Get the last read content"""
        return self.last_read_content if self.last_read_content else "No content read yet"