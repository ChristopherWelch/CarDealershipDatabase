from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer,Car,Brand,Dealer
# Create your views here.
def index(request):
    querySet = Customer.objects.all()
    context = {
        "object_list": querySet,
        "title": "List"
    }
    return render(request,"index.html",context)
