# In chatbot_app/models.py
from django.db import models

class ChatMessage(models.Model):
    user_message = models.TextField()
    bot_response = models.TextField()

    def __str__(self):
        return f"User: {self.user_message}, Bot: {self.bot_response}"
