from django.contrib import admin

# Register your models here.

from .models import Car, Brand, Dealer, Customer

admin.site.register(Car)
#admin.site.register(Company)
admin.site.register(Brand)
admin.site.register(Dealer)
admin.site.register(Customer)
