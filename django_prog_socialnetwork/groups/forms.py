from django import forms
from groups.models import CustomGroup

class GroupForm(forms.ModelForm):
    class Meta:
        model = CustomGroup
        fields = (
            'name',
            'description',
            'members',
            'moderators',
        )