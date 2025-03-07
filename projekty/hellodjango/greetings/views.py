from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.utils import timezone

# Create your views here.
def hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello Django!")


def hello_name(request: HttpRequest, name, wiek=None) -> HttpResponse:
    if wiek:
        now = timezone.now()

        return HttpResponse(f"Hello {name} ({now.year - int(wiek)})!")

    return HttpResponse(f"Hello {name}!")

def hello_last_name(request, name, lastname):
    return HttpResponse(f"Hello {name} {lastname}!")