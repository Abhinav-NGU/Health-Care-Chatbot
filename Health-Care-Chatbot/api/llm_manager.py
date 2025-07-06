from django.conf import settings
from langchain_community.llms import Ollama

class LLMManager:
    _instance = None

    @staticmethod
    def get_instance():
        if LLMManager._instance is None:
            LLMManager._instance = Ollama(
                model="gemma3:4b",  # Use the model you've pulled locally
                temperature=0.0,
                base_url="http://localhost:11434"  
            )
        return LLMManager._instance
