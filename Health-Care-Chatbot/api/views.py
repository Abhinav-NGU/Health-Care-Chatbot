from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .forms import ChatForm
from .models import ChatMessage, Prompt
from .llm_manager import LLMManager
from django.http import JsonResponse
from langchain.prompts import PromptTemplate
from decouple import config
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def chatbot_api(request):
    try:
        user_message = request.data.get('user_message', '').strip()
        if not user_message:
            return Response({'error': 'User message is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the prompt from the database (admin-editable)
        try:
            prompt_obj = Prompt.objects.first()
            if not prompt_obj:
                return Response({'error': 'Prompt not found. Please add a prompt in the admin panel.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Prompt.DoesNotExist:
            return Response({'error': 'Prompt not found. Please add a prompt in the admin panel.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        prompt = PromptTemplate.from_template(prompt_obj.text)
        prompt_text = prompt.format_prompt(user_message=user_message).to_string()

        # Get LLM response
        llm = LLMManager.get_instance()
        bot_response = llm.invoke(prompt_text)

        # Save to database
        ChatMessage.objects.create(user_message=user_message, bot_response=bot_response)

        return Response({'bot_response': bot_response}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# def test_api_key(request):
#     api_key = config('GROQ_API_KEY', default=None)
#     if api_key:
#         return JsonResponse({'status': 'success', 'api_key': api_key})
#     return JsonResponse({'status': 'error', 'message': 'API key not found'})

