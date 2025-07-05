from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm
)
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'avatar',
            'bio',
            'age'
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'username',
        )

class UserProfileEdit(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'avatar',
            'bio',
            'age'
        )