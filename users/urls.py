from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_posts, name='my_posts'),
    path('<int:post_id>/edit', views.edit_story, name='edit_story'),
    path('<int:post_id>/delete', views.delete_story, name='delete_story'),
]