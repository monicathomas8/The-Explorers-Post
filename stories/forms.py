from django import forms
from .models import Story

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'content', ] 
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        }