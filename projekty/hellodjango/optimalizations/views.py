from django.http import HttpResponse
from django.shortcuts import render
from .services import calculate
# Create your views here.

def spalanie(request, distance, price_per_l, l_per_100):
    return HttpResponse(calculate(int(distance), float(price_per_l), float(l_per_100)))
