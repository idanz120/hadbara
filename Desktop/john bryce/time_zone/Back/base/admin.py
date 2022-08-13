from django.contrib import admin
from .models import Products
from .models import Supplier
from .models import Customers
from .models import Orders
from .models import Order_Details
from .models import Stores

# Register your models here.

admin.site.register(Products)
admin.site.register(Supplier)
admin.site.register(Customers)
admin.site.register(Orders)
admin.site.register(Order_Details)
admin.site.register(Stores)