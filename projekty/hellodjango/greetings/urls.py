
from django.urls import path


from greetings.views import hello, hello_name, hello_last_name, test



urlpatterns = [

    path("", hello),
    path("test/", test),
    path("<name>/", hello_name),
    path("<name>/<int:wiek>", hello_name),
    path("<name>/<lastname>", hello_last_name),
]
