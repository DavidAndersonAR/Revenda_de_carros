from django.shortcuts import render
from .models import Car

# Create your views here.


def cars_views(request):

    search = request.GET.get('search')

    cars = Car.objects.filter(model__contains=search)

    return render(
        request,
        'cars.html',
        {'cars':cars} )