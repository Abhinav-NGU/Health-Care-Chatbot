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
    - Behave like a nurse first step before meeting doctor.
    - **Prioritize Health:** Provide accurate and useful health information while prioritizing user well-being.
    - **Avoid Medical Diagnosis:** Do not give medical diagnoses. Always recommend consulting a doctor for serious concerns.
    - **General Health Advice:** Provide tips on diet, exercise, stress management, and other general health topics when relevant.
    - **Symptom Checker:** Ask basic questions about symptoms and suggest potential causes. Always emphasize consulting a doctor for a proper diagnosis and treatment.
    - **Quick Action for Minor Issues:** If the issue appears minor, offer simple remedies, precautions, or over-the-counter medication advice early in the conversation.
    - **Accurate Information:** Ensure that your responses are up-to-date and reliable.
    - **Ask Clarifying Questions:** Ask relevant and concise questions to understand the issue. Don't go too far with the questions, stop once you have enough information to provide helpful advice and also when customer is satisfied.
    - **Clarity and Conciseness:** Use straightforward language to deliver clear and concise responses.
    - **Stay Focused:** Do not engage in non-medical discussions or unrelated topics.
    - **Avoid Overpromising:** Do not make guarantees or promises that cannot be fulfilled.

    ### User Input: {user_message}

    ### Response:
    """
)


def chatbot(request):
    # Handle GET requests (for page load)
    if request.method == 'GET':
        form = ChatForm()
        return render(request, 'chatbot.html', {'form': form})

    # Handle POST requests (when user submits a message)
    elif request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['user_message']
            
            # Format the prompt with the user's message
            prompt_text = prompt.format(user_message=user_message)
            
            # Use the initialized LLM to get the response with the formatted prompt
            llm = LLMManager.get_instance()  # Get the initialized LLM
            bot_response = llm.invoke(prompt_text)  # Call the LLM's invoke method
            
            # Ensure the response is a string (if it's already a string, no need to decode)
            bot_response_text = bot_response.content if isinstance(bot_response.content, str) else bot_response.content.decode()

            # Save the chat history to the database
            ChatMessage.objects.create(user_message=user_message, bot_response=bot_response_text)

            # Return the response back in the form of JSON
            return JsonResponse({'bot_response': bot_response_text})

    # If the method is neither GET nor POST, return an error
    return JsonResponse({"error": "Invalid request method"}, status=405)


# def test_api_key(request):
#     api_key = config('GROQ_API_KEY', default=None)
#     if api_key:
#         return JsonResponse({'status': 'success', 'api_key': api_key})
#     return JsonResponse({'status': 'error', 'message': 'API key not found'})

