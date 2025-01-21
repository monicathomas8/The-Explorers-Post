from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def landing_page(request):
    """
    Renders the landing page.
    """
    return render(request, 'landing_page.html')


def contact(request):
    """
    Handles the contact form submission and displays the contact page.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for reaching out! We'll get back to you soon."
            )
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
