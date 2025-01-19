from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def landing_page(request):
    return render(request, 'landing_page.html')


def contact(request):
    if request.method == 'POST':
        form= ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 
            "Thank you for reaching out! We'll get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})