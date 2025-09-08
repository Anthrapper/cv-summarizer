from typing import Dict, List


class AppConfig:
    """Application configuration constants."""
    
    # App Info
    APP_TITLE = "CV Summarizer"
    APP_ICON = "📄"
    
    # Supported File Types
    SUPPORTED_FILE_TYPES = ['pdf', 'docx']
    
    # UI Messages
    MESSAGES = {
        'processing': 'Processing document...',
        'no_text_extracted': 'No text could be extracted from the document',
        'unsupported_file': 'Unsupported file type',
        'ollama_connection_error': 'Cannot connect to Ollama',
        'ollama_serve_info': 'Please start Ollama: `ollama serve`',
        'no_models_found': 'No models found. Please run: ollama pull <model>',
        'file_upload_help': 'Upload a CV in PDF or DOCX format'
    }