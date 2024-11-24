from django.conf import settings
from langchain_groq import ChatGroq

class LLMManager:
    _instance = None

    @staticmethod
    def get_instance():
        if LLMManager._instance is None:
            LLMManager._instance = ChatGroq(
                temperature=0,
                groq_api_key=settings.GROQ_API_KEY,
                model_name="llama-3.1-70b-versatile"
            )
        return LLMManager._instance
