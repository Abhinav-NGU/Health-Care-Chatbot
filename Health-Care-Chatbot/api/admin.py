from django.contrib import admin
from .models import ChatMessage, Prompt

# Register your models here
@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user_message', 'bot_response')
    search_fields = ('user_message', 'bot_response')
    list_filter = ('user_message',)
    ordering = ('-id',)

@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
