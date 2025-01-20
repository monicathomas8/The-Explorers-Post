from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Story
from .forms import StoryForm


def story_list(request):
    """
    Displays a list of published stories.
    """
    stories = Story.objects.filter(status=1)  # Fetch only published stories
    return render(request, 'story_list.html', {'stories': stories})


def story_detail(request, slug):
    """
    Displays the details of a specific story.
    """
    story = get_object_or_404(Story, slug=slug)
    return render(request, 'story_detail.html', {'story': story})


@login_required
def create_story(request):
    """
    Allows users to create and submit a new story.
    """
    if request.method == "POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.status = 0  # Defult to "draft"
            story.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Story submitted and awaiting approval'
            )

            return redirect('story_list')
    else:
        form = StoryForm()

    return render(request, 'create_story.html', {'form': form})
