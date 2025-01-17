from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from stories.models import Story
from stories.forms import StoryForm

# Create your views here.
@login_required
def my_posts(request):
    drafts = Story.objects.filter(author=request.user, status=0)  # Drafts
    published = Story.objects.filter(author=request.user, status=1)  # Published
    return render(request, 'my_posts.html', {'drafts': drafts, 'published': published})


@login_required
def edit_story(request, post_id):
    """
    View to edit a story by the logged-in user
    """
    story = get_object_or_404(Story, id=post_id, author=request.user)  # Ensure the user owns the story
    if request.method == "POST":
        form = StoryForm(data=request.POST, instance=story)  # Prepopulate the form with story data
        if form.is_valid():
            story = form.save()  # Save the updated story
            messages.add_message(request, messages.SUCCESS, 'Story updated successfully!')
            return redirect('my_posts')  # Redirect to user's stories page
        else:
            messages.add_message(request, messages.ERROR, 'Error updating the story.')
    else:
        form = StoryForm(instance=story)  # Load the existing story into the form

    return render(request, 'edit_story.html', {'form': form, 'story': story})


@login_required
def delete_story(request, post_id):
    """
    View to delete a story by the logged-in user
    """
    story = get_object_or_404(Story, id=post_id, author=request.user)  # Ensure the user owns the story
    if request.method == "POST":
        story.delete()  # Delete the story
        messages.add_message(request, messages.SUCCESS, 'Story deleted successfully!')
        return redirect('my_posts')  # Redirect to user's stories page

    return render(request, 'delete_story.html', {'story': story})
