from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from stories.models import Story
from stories.forms import StoryForm


@login_required
def my_posts(request):
    """
    Displays the user's draft and published stories.
    """
    drafts = Story.objects.filter(author=request.user, status=0)
    published = Story.objects.filter(author=request.user, status=1)
    return render(request,
                  'my_posts.html', {'drafts': drafts, 'published': published})


@login_required
def edit_story(request, post_id):
    """
    View to edit a story by the logged-in user
    """
    story = get_object_or_404(Story, id=post_id, author=request.user)
    if request.method == "POST":
        form = StoryForm(data=request.POST, instance=story)
        if form.is_valid():
            story = form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Story updated successfully!')
            return redirect('my_posts')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating the story.')
    else:
        form = StoryForm(instance=story)

    return render(request, 'edit_story.html', {'form': form, 'story': story})


@login_required
def delete_story(request, post_id):
    """
    View to delete a story by the logged-in user
    """
    story = get_object_or_404(Story, id=post_id, author=request.user)
    if request.method == "POST":
        story.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Story deleted successfully!')
        return redirect('my_posts')

    return render(request, 'delete_story.html', {'story': story})
