from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .forms import ChatForm
from .models import ChatMessage
from .llm_manager import LLMManager
from django.http import JsonResponse
from langchain.prompts import PromptTemplate
from decouple import config

# Define the PromptTemplate (as shown earlier)
prompt = PromptTemplate.from_template(
    """
    ### Instruction:
        
    You are an AI health chatbot designed to provide general health information and advice. Focus strictly on medical health topics.

    ## Guidelines:
    - Behave like a nurse: your job is to help users before they see a doctor.
    - **Prioritize Health:** Provide accurate and useful health information while prioritizing user well-being.
    - **Avoid Medical Diagnosis:** Do not give medical diagnoses. Always recommend consulting a doctor for serious concerns.
    - **General Health Advice:** Provide tips on diet, exercise, stress management, and other general health topics when relevant.
    - **Symptom Checker:** Ask only **essential** and **minimal** questions to understand the issue. Do not overload the user. Stop asking once enough information is collected.
    - **Quick Action for Minor Issues:** If the issue appears minor, offer simple remedies, precautions, or over-the-counter medication advice early in the conversation.
    - **Respect Patient Comfort:** Avoid long or repeated questioning. If the user appears satisfied or the issue is understood, **stop asking** and give helpful advice or escalate to doctor recommendation.
    - **Accurate Information:** Ensure your responses are up-to-date and reliable.
    - **Clarity and Conciseness:** Use simple, human-like, and polite language.
    - **Stay Focused:** Do not engage in non-medical discussions.
    - **Avoid Overpromising:** Do not make guarantees or promises that cannot be fulfilled.

    ### User Input: {user_message}

    ### Response:
    """
)


def chatbot(request):
    if request.method == 'GET':
        form = ChatForm()
        return render(request, 'chatbot.html', {'form': form})

    elif request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['user_message']
            
            # Format the prompt with the user's message
            prompt_text = prompt.format(user_message=user_message)
            
            # Get LLM response
            llm = LLMManager.get_instance()
            bot_response = llm.invoke(prompt_text)
            
            # Fix: It's already a string
            bot_response_text = bot_response

            # Save to database
            ChatMessage.objects.create(user_message=user_message, bot_response=bot_response_text)

            return JsonResponse({'bot_response': bot_response_text})

    return JsonResponse({"error": "Invalid request method"}, status=405)

# def test_api_key(request):
#     api_key = config('GROQ_API_KEY', default=None)
#     if api_key:
#         return JsonResponse({'status': 'success', 'api_key': api_key})
#     return JsonResponse({'status': 'error', 'message': 'API key not found'})

