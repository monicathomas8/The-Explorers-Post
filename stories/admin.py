from django.contrib import admin
from .models import Story
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_status_display', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ('title', 'content')
