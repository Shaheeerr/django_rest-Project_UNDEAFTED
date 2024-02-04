from django.contrib import admin
from .models import *

@admin.register(Order,OrderItem)   #register with admin.site register
class MyModelAdmin(admin.ModelAdmin):
    pass

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id', 'customer', 'order_date', 'total_amount']


# @admin.register(OrderDetail)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id', 'order', 'product', 'order_price','qty']