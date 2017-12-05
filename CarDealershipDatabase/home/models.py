from django.db import models
# Create your models here.
class Car(models.Model):
    vin = models.CharField(max_length=17, primary_key=True)
    make = models.CharField(max_length=200)
    year = models.IntegerField()
    color = models.CharField(max_length=200)
    previous_owner = models.CharField(max_length=200)
    source = models.FileField(upload_to='cars/%Y/%m/%d/',default="abc")

    def __str__(self):
        return self.vin + ' ' + self.make + ' ' + str(self.year) + ' ' + self.color 

#class Company(models.Model):
 #   company_name = models.CharField(max_length=200, primary_key=True)
  #  brand = models.CharField(max_length=200)

   # def __str__(self):
    #    return self.company_name + ' ' + self.brand
    
class Brand(models.Model):
    company_name = models.CharField(max_length=200)
    make = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name + ' ' + self.make
        
    
class Dealer(models.Model):
    dealer_id = models.IntegerField(primary_key=True)
    customers = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return str(self.dealer_id) + ' ' + self.customers + ' ' + self.address + ' ' + self.phone


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    purchase = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return str(self.customer_id) + ' ' + self.name + ' ' + self.purchase + ' ' + self.address + ' ' + self.phone
