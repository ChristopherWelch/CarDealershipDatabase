from django.contrib import admin

# Register your models here.

from .models import Car, Company, Brand, Dealer, Customers

admin.site.register(Car)
admin.site.register(Company)
admin.site.register(Brand)
admin.site.register(Dealer)
admin.site.register(Customers)
