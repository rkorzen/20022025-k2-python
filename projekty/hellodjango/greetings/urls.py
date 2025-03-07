
from django.urls import path


from greetings.views import hello, hello_name, hello_last_name



urlpatterns = [

    path("", hello),
    path("<name>", hello_name),
    path("<name>/<int:wiek>", hello_name),
    path("<name>/<lastname>", hello_last_name),
]
