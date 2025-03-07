from django.urls import path
from . import views

urlpatterns = [
    path("spalanie/<distance>/<price_per_l>/<l_per_100>/", views.spalanie)

]