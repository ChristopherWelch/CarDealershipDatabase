from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Customer,Car,Brand,Dealer
from django.template import loader


# Create your views here.
def index(request):
    querySet = Car.objects.all()
    template = loader.get_template('home/index.html')
    context = {
        "all_cars" : querySet,
    }
    return HttpResponse(template.render(context,request))

def detail(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        raise Http404("No record for this vehicle")
    return render(request, 'home/detail.html', {'car' : car})

