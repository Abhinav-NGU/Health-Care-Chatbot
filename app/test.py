from django.http import JsonResponse
from decouple import config

def test_api_key(request):
    api_key = config('GROQ_API_KEY', default=None)
    if api_key:
        return JsonResponse({'status': 'success', 'api_key': api_key})
    return JsonResponse({'status': 'error', 'message': 'API key not found'})
