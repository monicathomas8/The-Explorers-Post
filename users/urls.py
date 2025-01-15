from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_posts, name='my_posts'),
    path('edit-post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete_post'),
]