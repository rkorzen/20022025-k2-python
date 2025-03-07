from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.utils import timezone
from django.template import loader
# Create your views here.
def hello(request: HttpRequest) -> HttpResponse:

    koncowki = ["/greetings/", "/greetings/Rafał", "/greetings/Rafał/30", "/greetings/Rafał/Korzeniewski" ]

    slownik = {"a": "wartosc dla a", "b": "dijqwodcoj"}

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return f"{self.name} ({self.age})"

        def odezwij_sie(self):
            return "Hej to ja!"


    p = Person("Rafał", 30)

    return render(request, "greetings/hello_name.html", {"name": "Django", "koncowki": koncowki, "slownik": slownik, "osoba": p})


def hello_name(request: HttpRequest, name, wiek=None) -> HttpResponse:
    template_name = "greetings/hello_name.html"
    now = timezone.now()
    context = {"name": name, "wiek": None}
    if wiek:
        context["wiek"] = now.year - wiek
        content = loader.render_to_string(template_name, context, request)
        return HttpResponse(content)

    return render(request, template_name, context)

def hello_last_name(request, name, lastname):
    return render(
        request,
        "greetings/hello_name.html",
        {"name": name, "lastname": lastname}
    )

def test(request):
    return render(
        request,
        "base.html",
        {}
    )