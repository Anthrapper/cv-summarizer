import streamlit as st
import sys
import os

# Add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.components.resume_summarizer import ResumeSummarizer
from src.components.summary_result import SummaryResult
from src.components.ui import UI
from src.components.file_handler import FileHandler
from src.components.progress_tracker import ProgressTracker
from src.utils.css_styler import CSSStyler
from src.utils.validation_utils import ValidationUtils
from src.utils.settings_loader import SettingsLoader

# Global instances
css_styler = CSSStyler()
validator = ValidationUtils()
settings_loader = SettingsLoader()


class ResumeSummarizerApp:
    """
    Main application class for the AI Resume/CV Summarizer.
    
    Orchestrates the UI components and summarizer logic.
    """
    
    def __init__(self):
        """Initialize the application."""
        # Apply custom CSS styles
        css_styler.apply_styles()
        
        # Configure page
        st.set_page_config(
            page_title="CV Summarizer",
            page_icon="📄",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # Load settings from external file
        self.settings = settings_loader.load_settings()
        
        # Initialize summarizer with settings
        self.summarizer = ResumeSummarizer(settings=self.settings)
        
        # Initialize UI components
        self.ui = UI()
        self.file_handler = FileHandler()
            
    def run(self):
        """Run the main application loop."""
        try:
            # Render UI components
            self.ui.render_header()
            self.ui.render_sidebar_settings(self.summarizer)
            
            # Handle file upload
            uploaded_file = self.ui.render_file_uploader()
            
            if uploaded_file is not None:
                self._process_uploaded_file(uploaded_file)
            
            # Render instructions
            self.ui.render_instructions()
            
        except Exception as e:
            self.ui.render_error(f"An unexpected error occurred: {str(e)}")
    
    def _process_uploaded_file(self, uploaded_file):
        """
        Process an uploaded file.
        
        Args:
            uploaded_file: Streamlit uploaded file object
        """
        try:
            # Display file information
            self.ui.render_file_info(uploaded_file)
            
            # Process button
            if self.ui.render_process_button():
                self._generate_summary(uploaded_file)
                
        except Exception as e:
            self.ui.render_error(f"Error processing file: {str(e)}")
    
    def _generate_summary(self, uploaded_file):
        """
        Generate summary for uploaded file.
        
        Args:
            uploaded_file: Streamlit uploaded file object
        """
        progress_tracker = ProgressTracker()
        temp_file_path = None
        
        try:
            with st.spinner("Processing document..."):
                # Save uploaded file temporarily
                temp_file_path = self.file_handler.save_uploaded_file(uploaded_file)
                
                # Get file extension
                file_extension = self.file_handler.get_file_extension(uploaded_file.name)
                
                # Define progress callback for chunked processing
                def progress_callback(current, total, text):
                    progress_tracker.update_progress(current, total, text)
                
                # Get the prompt from settings
                custom_prompt = settings_loader.get_prompt(self.settings)
                
                # Process document with progress callback
                result = self.summarizer.process_document(
                    file_path=temp_file_path,
                    file_type=file_extension,
                    progress_callback=progress_callback,
                    custom_prompt=custom_prompt
                )
                
                # Handle result
                if result.success:
                    self._display_summary_result(result, uploaded_file.name)
                else:
                    self.ui.render_error(f"Error generating summary: {result.error}")
                
        except Exception as e:
            self.ui.render_error(f"Error generating summary: {str(e)}")
            
        finally:
            # Clean up
            progress_tracker.finish()
            if temp_file_path:
                self.file_handler.cleanup_temp_file(temp_file_path)
    
    def _display_summary_result(self, result: SummaryResult, original_filename: str):
        """
        Display the generated summary result.
        
        Args:
            result: SummaryResult object
            original_filename: Original filename for download
        """
        # Validate summary length using current settings
        summary_settings = settings_loader.get_summary_settings(self.settings)
        validation = validator.validate_summary_length(result.summary, summary_settings['min_length'], summary_settings['max_length'])
        
        # Display summary
        self.ui.render_summary_result(result.summary)
        
        # Display download button
        self.ui.render_download_button(result.summary, original_filename)
        
  

def main():
    """Main entry point for the application."""
    try:
        app = ResumeSummarizerApp()
        app.run()
    except Exception as e:
        st.error(f"A critical error occurred. Please restart the application.")


if __name__ == "__main__":
    main()