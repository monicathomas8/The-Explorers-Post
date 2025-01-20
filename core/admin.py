from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing contact form submissions.
    """
    list_display = ('name', 'email', 'subject', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'subject', 'message')
