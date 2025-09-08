import os
import tempfile
import streamlit as st


class FileHandler:
    """Handles file operations for uploaded documents."""
    
    def save_uploaded_file(self, uploaded_file) -> str:
        """
        Save uploaded file to temporary location.
        
        Args:
            uploaded_file: Streamlit uploaded file object
            
        Returns:
            str: Path to the saved temporary file
        """
        file_extension = self.get_file_extension(uploaded_file.name)
        with tempfile.NamedTemporaryFile(
            delete=False, 
            suffix=f".{file_extension}"
        ) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            return tmp_file.name
    
    def get_file_extension(self, filename: str) -> str:
        """
        Extract file extension from filename.
        
        Args:
            filename: Name of the file
            
        Returns:
            str: File extension
        """
        return filename.split('.')[-1].lower()
    
    def cleanup_temp_file(self, file_path: str):
        """
        Clean up temporary file.
        
        Args:
            file_path: Path to the temporary file to clean up
        """
        if os.path.exists(file_path):
            os.unlink(file_path)
    
    