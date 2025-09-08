import streamlit as st
import os


class CSSStyler:
    """CSS styling utilities."""
    
    @staticmethod
    def apply_styles():
        """Apply custom CSS styles to the Streamlit app."""
        css_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'styles.css')
        
        with open(css_file_path, 'r') as f:
            css_content = f.read()
        
        # Wrap CSS in style tags for Streamlit
        styled_css = f"<style>{css_content}</style>"
        st.markdown(styled_css, unsafe_allow_html=True)