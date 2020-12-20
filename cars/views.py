from django.shortcuts import render
from .models import  Car

# Create your views here.
def index(request):
    new_cars = Car.objects.filter(category='New')[:6]
    used_cars = Car.objects.filter(category='Used')[:6]

    context = {
        'new_cars': new_cars,
        'used_cars': used_cars,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

