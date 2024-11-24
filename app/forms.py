from django import forms

class ChatForm(forms.Form):
    user_message = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Type your message here...', 'class': 'form-control'}),
        max_length=500,
    )
