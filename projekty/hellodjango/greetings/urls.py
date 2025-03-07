
from django.urls import path


from greetings.views import hello, hello_name, hello_last_name, test



urlpatterns = [

    path("", hello, name="hello"),
    path("test/", test, name="test"),
    path("<name>/", hello_name, name="hello_name"),
    path("<name>/<int:wiek>", hello_name, name="hello_name_with_age"),
    path("<name>/<lastname>", hello_last_name, name="hello_last_name"),
]
