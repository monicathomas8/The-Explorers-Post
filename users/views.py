from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from stories.models import Story
from stories.forms import StoryForm

# Create your views here.
@login_required
def my_posts(request):
    drafts = Story.objects.filter(author=request.user, status=0)  # Drafts
    published = Story.objects.filter(author=request.user, status=1)  # Published
    return render(request, 'my_posts.html', {'drafts': drafts, 'published': published})

@login_required
def edit_post(request, post_id):
    story = get_object_or_404(Story, id=post_id, author=request.user)
    if request.method == "POST":
        form = StoryForm(request.POST, instance=story)
        if form.is_valid():
            form.save()
            return redirect('my_posts')  # Redirect to the user's posts
    else:
        form = StoryForm(instance=story)
    return render(request, 'users/edit_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    story = get_object_or_404(Story, id=post_id, author=request.user)
    if request.method == "POST":
        story.delete()
        return redirect('my_posts')
    return render(request, 'users/delete_post.html', {'story': story})
