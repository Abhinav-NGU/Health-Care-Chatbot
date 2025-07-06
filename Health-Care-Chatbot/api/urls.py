from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('chatbot/', views.chatbot_api, name='chatbot_api'), 
]
