from django.apps import AppConfig
from .llm_manager import LLMManager  # Assuming you created LLMManager in `app/llm_manager.py`

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        # Initialize the LLM when the app is ready
        LLMManager.get_instance()
