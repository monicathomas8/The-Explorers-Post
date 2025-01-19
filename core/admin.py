from django.contrib import admin
from .models import Contact


"""
Admin configuration for managing contact form submissions.
"""
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'subject', 'message')
