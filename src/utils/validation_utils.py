from typing import Dict, Any


class ValidationUtils:
    """Validation utilities for the application."""
    
    def validate_summary_length(self, summary: str, min_length: int, max_length: int) -> Dict[str, Any]:
        """
        Validate summary length requirements.
        
        Args:
            summary: Summary text to validate
            min_length: Minimum required length
            max_length: Maximum allowed length
            
        Returns:
            Dict with validation results
        """
        length = len(summary)
        min_required = min_length
        max_allowed = max_length
        is_valid = min_required <= length <= max_allowed
        
        return {
            'is_valid': is_valid,
            'length': length,
            'min_required': min_required,
            'max_allowed': max_allowed,
            'needs_padding': length < min_required,
            'needs_truncation': length > max_allowed
        }