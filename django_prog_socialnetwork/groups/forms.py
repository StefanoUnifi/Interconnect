from django import forms
from .models import CustomGroup

class GroupForm(forms.ModelForm):
    class Meta:
        model = CustomGroup
        fields = (
            'name',
            'description',
            'members',
            'moderators',
        )