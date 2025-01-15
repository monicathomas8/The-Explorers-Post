from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Story
from .forms import StoryForm

# Create your views here.

def story_list(request):
    stories = Story.objects.filter(status=1)  # Fetch only published stories
    return render(request, 'story_list.html', {'stories': stories})

def story_detail(request, slug):
    story = get_object_or_404(Story, slug=slug)
    return render(request, 'story_detail.html', {'story': story})

@login_required
def create_story(request):
    if request.method == "POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user  # Set the current logged-in user as the author
            story.status = 0  # Default to "Draft" or adjust as needed
            story.save()
            return redirect('story_list')  # Redirect to the list of stories
    else:
        form = StoryForm()

    return render(request, 'create_story.html', {'form': form})