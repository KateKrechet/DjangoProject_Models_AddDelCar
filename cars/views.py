from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def index(req):
    if req.POST:
        # показываем, что не заполнено, если нажали отправить, а форма не заполнена
        car_info = CarForm(req.POST)
        bd = Car.objects.all()
        if car_info.is_valid():
            print('ok')
            car = Car()
            car.brand = req.POST.get('brand1')
            car.producer = req.POST.get('producer1')
            car.year = req.POST.get('year1')
            car.number = req.POST.get('number1')
            car.save()
            return redirect('home')

        else:
            print('neok')

    else:
        car_info = CarForm()
        bd = Car.objects.all()
    data = {'form': car_info, 'database': bd}
    return render(req, "index.html", context=data)


def delete(req, ids):
    car = Car.objects.get(id=ids)
    car.delete()
    return redirect('home')
