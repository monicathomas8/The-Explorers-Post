from django.urls import path
from . import views

urlpatterns = [
    path('my-posts/', views.my_posts, name='my_posts'),
]