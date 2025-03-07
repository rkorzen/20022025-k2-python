from django.shortcuts import render

from .services import calculate


# Create your views here.

def spalanie(request, distance, price_per_l, l_per_100):

    result = calculate(int(distance), float(price_per_l), float(l_per_100))
    context = {
        'dystans': distance,
        "koszt": price_per_l,
        "spalanie": l_per_100,
        "result": result
    }

    return render(request, 'optimalizations/spalanie.html', context)

