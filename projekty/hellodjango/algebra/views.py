from django.shortcuts import render
from django.http import HttpResponse, Http404

from .services import Calculator


# Create your views here.


def calculator(request, op, a, b):

    if op not in ["add", "sub", "mul", "div"]:
        raise Http404

    calculator = Calculator()

    result = calculator.calculate(op, a, b)

    return render(request, 'algebra/result.html', {'result': result, "op": op, "a": a, "b": b})

