from django.shortcuts import render
from .models import Contact
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, "base.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        contact = Contact.objects.create(name=name, email=email, message=message)
        messages.success(request, "Wiadomość została zapisana")


    return render(request, "home/contact.html")