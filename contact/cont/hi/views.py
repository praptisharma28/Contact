# hi/views.py
from django.shortcuts import render
from .models import ContactForm

def contact_form(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']

        # Save the form data to the database
        contact_entry = ContactForm(first_name=first_name, last_name=last_name, email=email, message=message)
        contact_entry.save()

    return render(request, 'contact.html')
