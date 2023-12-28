from django import forms
from .models import User, UserProfile

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
