from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from stories.models import Story

# Create your views here.
@login_required
def my_posts(request):
    drafts = Story.objects.filter(author=request.user, status=0)  # Drafts
    published = Story.objects.filter(author=request.user, status=1)  # Published
    return render(request, 'my_posts.html', {'drafts': drafts, 'published': published})