from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *

class ProductVariantInline(admin.StackedInline):   #set StackedInline for ProductVariantInline
    model = ProductVariant
    extra = 1 

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariantInline]     #inline the ProductVarient

admin.site.register(Product, ProductAdmin)    

@admin.register(Category, Brand, Size,ProductVariant,Cart,CartItem)   #register with admin.site register
class MyModelAdmin(admin.ModelAdmin):
    pass










