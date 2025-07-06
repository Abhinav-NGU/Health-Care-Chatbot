# In chatbot_app/models.py
from django.db import models

class Prompt(models.Model):
    name = models.CharField(max_length=100, unique=True, default="default")
    text = models.TextField()

    def __str__(self):
        return self.name

class ChatMessage(models.Model):
    user_message = models.TextField()
    bot_response = models.TextField()

    def __str__(self):
        return f"User: {self.user_message}, Bot: {self.bot_response}"
