from django.urls import path

from . import views

urlpatterns = [
    path("algebra/<op>/<int:a>/<int:b>", views.calculator),

]