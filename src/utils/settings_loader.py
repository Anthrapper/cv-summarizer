import json
import os
from typing import Dict, Any, Optional


class SettingsLoader:
    """Loads settings from external JSON file."""
    
    def __init__(self, settings_file: str = "settings.json"):
        """
        Initialize settings loader.
        
        Args:
            settings_file: Path to settings JSON file
        """
        self.settings_file = settings_file
        self._settings_cache = None
    
    def load_settings(self) -> Dict[str, Any]:
        """
        Load settings from JSON file.
        
        Returns:
            Dict[str, Any]: Loaded settings dictionary
        """
        if self._settings_cache:
            return self._settings_cache
        
        with open(self.settings_file, 'r') as f:
            config = json.load(f)
        
        self._settings_cache = config
        return config
    
    def get_prompt(self, settings: Dict[str, Any]) -> str:
        """
        Get the prompt from settings.
        
        Args:
            settings: Current application settings dictionary
            
        Returns:
            str: The prompt to use
        """
        prompt = settings.get('prompt', '')
        
        if not prompt:
            raise ValueError("No prompt found in settings")
        
        # Replace placeholders with actual values
        min_length = settings.get('summary_settings', {}).get('min_length', 430)
        max_length = settings.get('summary_settings', {}).get('max_length', 500)
        
        return prompt.replace("{min_length}", str(min_length)).replace("{max_length}", str(max_length))
    
    def get_summary_settings(self, settings: Dict[str, Any]) -> Dict[str, int]:
        """
        Get summary settings from configuration.
        
        Args:
            settings: Current application settings dictionary
            
        Returns:
            Dict[str, int]: Summary settings (min_length, max_length)
        """
        return settings.get('summary_settings', {
            'min_length': 430,
            'max_length': 500
        })
    
    def get_model_settings(self, settings: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get model settings from configuration.
        
        Args:
            settings: Current application settings dictionary
            
        Returns:
            Dict[str, Any]: Model settings (temperature, max_tokens, chunk_size)
        """
        return settings.get('model_settings', {
            'temperature': 0.2,
            'max_tokens': 600,
            'chunk_size': 3000
        })
    
    def get_ollama_settings(self, settings: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get Ollama settings from configuration.
        
        Args:
            settings: Current application settings dictionary
            
        Returns:
            Dict[str, Any]: Ollama settings (base_url, timeout)
        """
        return settings.get('ollama_settings', {
            'base_url': 'http://localhost:11434',
            'timeout': 60
        })