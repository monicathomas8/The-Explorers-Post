from django import forms
from .models import Story
from django_summernote.widgets import SummernoteWidget

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'location', 'content', ] 
        widgets = {
            'content': SummernoteWidget(),
        }