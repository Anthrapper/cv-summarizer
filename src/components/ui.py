import streamlit as st
from src.utils.app_config import AppConfig


class UI:
    """Collection of UI components for the resume summarizer app."""
    
    @staticmethod
    def render_header():
        """Render the main header of the application."""
        st.markdown("""
        <div class="main-header">
            <h1>📄 CV Summarizer</h1>
            <p>Upload CVs to get recruiter-focused AI summaries</p>
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def render_sidebar_settings(summarizer):
        """
        Render sidebar settings and model selection.
        
        Args:
            summarizer: ResumeSummarizer instance
        """
        st.sidebar.title("Settings")
        
        # Ollama endpoint info
        ollama_endpoint = getattr(summarizer, 'ollama_base_url', 'http://localhost:11434')
        st.sidebar.markdown(f"**Ollama Endpoint:** `{ollama_endpoint}`")
        
        # Model selection
        try:
            available_models = summarizer.get_available_models()
            
            if available_models:
                selected_model = st.sidebar.selectbox(
                    "Select Model",
                    available_models,
                    index=available_models.index(summarizer.model) if summarizer.model in available_models else 0
                )
                
                # Update summarizer model if changed
                if selected_model != summarizer.model:
                    summarizer.model = selected_model
                
            else:
                st.sidebar.warning(AppConfig.MESSAGES['no_models_found'])
                
        except Exception as e:
            st.sidebar.error(f"{AppConfig.MESSAGES['ollama_connection_error']}: {str(e)}")
            st.sidebar.info(AppConfig.MESSAGES['ollama_serve_info'])
    
    @staticmethod
    def render_file_uploader():
        """
        Render the file upload component.
        
        Returns:
            Uploaded file or None
        """
        st.subheader("Upload CV")
        
        uploaded_file = st.file_uploader(
            "Choose a PDF or DOCX file",
            type=AppConfig.SUPPORTED_FILE_TYPES,
            help=AppConfig.MESSAGES['file_upload_help']
        )
        
        return uploaded_file
    
    @staticmethod
    def render_file_info(uploaded_file):
        """
        Display file information.
        
        Args:
            uploaded_file: The uploaded file object
        """
        file_info = {
            "Filename": uploaded_file.name,
            "Size": f"{uploaded_file.size / 1024:.1f} KB",
            "Type": uploaded_file.type
        }
        
        st.json(file_info)
    
    @staticmethod
    def render_process_button() -> bool:
        """
        Render the process button.
        
        Returns:
            bool: True if button was clicked
        """
        return st.button("Generate Summary", type="primary")
    
    @staticmethod
    def render_summary_result(summary: str):
        """
        Render the generated summary.
        
        Args:
            summary: The generated summary text
        """
        st.subheader("AI Summary")
        st.markdown(f"""
        <div class="summary-card">
            {summary.replace(chr(10), '<br>')}
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def render_download_button(summary: str, filename: str):
        """
        Render download button for summary.
        
        Args:
            summary: Summary text to download
            filename: Original filename for naming the download
        """
        st.download_button(
            label="Download Summary",
            data=summary,
            file_name=f"summary_{filename.split('.')[0]}.txt",
            mime="text/plain"
        )
    
    @staticmethod
    def render_error(message: str):
        """
        Render error message.
        
        Args:
            message: Error message to display
        """
        st.error(message)
    
    @staticmethod
    def render_instructions():
        """Render usage instructions."""
        with st.expander("How to Use"):
            st.markdown("""
            1. **Upload**: Choose a PDF or DOCX file containing a CV
            2. **Select Model**: Choose your preferred model from the sidebar
            3. **Process**: Click "Generate Summary" to analyze the document
            4. **Review**: Read the AI-generated recruiter summary
            5. **Download**: Save the summary for future reference
            """)