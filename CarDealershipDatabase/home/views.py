from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Customer,Car,Brand,Dealer
from django.template import loader


# Create your views here.
def index(request):
    querySet = Brand.objects.all()
    template = loader.get_template('home/index.html')
    context = {
        "all_Brands" : querySet,
    }
    return HttpResponse(template.render(context,request))

def detail(request, brand_id):
    try:
        brand = Brand.objects.get(pk=brand_id)
    except Brand.DoesNotExist:
        raise Http404("No record for this brand")
    return render(request, 'home/detail.html', {'brand' : brand})

def carDetail(request,car_id):
    try:
        car = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        raise Http404("No record for this vehicle")
    return render(request, 'home/carDetail.html', {'car' : car})

