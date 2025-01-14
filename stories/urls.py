from django.urls import path
from . import views

urlpatterns = [
    path('', views.story_list, name='story_list'),  # URL for the list page
    path('create/', views.create_story, name='create_story'),
    path('<slug:slug>/', views.story_detail, name='story_detail'),
]
