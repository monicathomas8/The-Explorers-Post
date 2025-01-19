from django.contrib import admin
from .models import Story
from django_summernote.admin import SummernoteModelAdmin


"""
Admin configuration for managing stories in the admin panel.
"""
@admin.register(Story)
class StoryAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'get_status_display', 'created_on')
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    summernote_fields = ('content')

