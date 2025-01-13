from django.shortcuts import get_object_or_404, render
from .models import Story

# Create your views here.

def story_list(request):
    stories = Story.objects.filter(status=1)  # Fetch only published stories
    return render(request, 'story_list.html', {'stories': stories})

def story_detail(request, slug):
    story = get_object_or_404(Story, slug=slug)
    return render(request, 'story_detail.html', {'story': story})