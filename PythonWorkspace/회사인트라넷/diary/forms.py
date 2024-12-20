from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DiaryEntry

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ['date', 'content']
