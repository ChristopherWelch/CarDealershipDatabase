from django.db import models

# Create your models here.
class Car(models.Model):
    vin = models.CharField(max_length=17, primary_key=True)
    make = models.CharField(max_length=17)
    year = models.IntegerField()
    color = models.CharField(max_length=15)
    weight = models.IntegerField()
    engine = models.CharField(max_length=20)
    transmission = models.CharField(max_length=15)
    previous_owner = models.CharField(max_length=30)

class Company(models.Model):
    company_name = models.CharField(max_length=20, primary_key=True)
    brand = models.CharField(max_length=20)

class Brand(models.Model):
    company_name = models.CharField(max_length=20)
    make = models.CharField(max_length=17)

class Dealer(models.Model):
    dealer_id = models.IntegerField(primary_key=True)
    customers = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

class Customers(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    purchase = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    
