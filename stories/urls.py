from django.urls import path
from . import views

urlpatterns = [
    path('', views.story_list, name='story_list'),  # URL for the list page
    path('<slug:slug>/', views.story_detail, name='story_detail'),
]
