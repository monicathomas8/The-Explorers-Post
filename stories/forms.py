from django import forms
from .models import Story
from django_summernote.widgets import SummernoteWidget


class StoryForm(forms.ModelForm):
    class Meta:
        """
        A form for creating and editing stories.
        """
        model = Story
        fields = ['title', 'location', 'content', ]
        widgets = {
            'content': SummernoteWidget(),
        }
