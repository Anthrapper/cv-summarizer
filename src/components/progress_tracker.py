import streamlit as st
from typing import Optional


class ProgressTracker:
    """Handles progress tracking for long-running operations."""

    def __init__(self):
        """Initialize progress tracker."""
        self.progress_bar = None
        self.status_text = None

    def update_progress(
        self, current_step: int, total_steps: int, text: Optional[str] = None
    ):
        """
        Update progress tracking.

        Args:
            current_step: Current step number
            total_steps: Total number of steps
            text: Optional status text to display
        """
        if not self.progress_bar:
            self.progress_bar = st.progress(0)
        if not self.status_text:
            self.status_text = st.empty()

        progress = current_step / total_steps
        self.progress_bar.progress(progress)

        if text:
            self.status_text.text(text)
        else:
            self.status_text.text(f"Step {current_step}/{total_steps}")

    def finish(self):
        """Finish progress tracking and clean up."""
        if self.progress_bar:
            self.progress_bar.empty()
        if self.status_text:
            self.status_text.empty()

        self.progress_bar = None
        self.status_text = None
