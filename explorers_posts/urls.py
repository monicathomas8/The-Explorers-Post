from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('stories/', include('stories.urls')),  # Routes to Stories app URLs
    path('summernote/', include('django_summernote.urls')),
    path('users/', include('users.urls')),  # Routes to users app urls
    path('', include('core.urls')),  # Routes the root URL to the core app

]
