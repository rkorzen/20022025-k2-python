from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "base.html")

def about(request):
    return render(request, "home/about.html")