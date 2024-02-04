from rest_framework import serializers
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet


class CategorySerializer(serializers.ModelSerializer):    #category model
    
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):       #brand model serializer
    
    class Meta:
        model = Brand
        fields = ['name']

class SizeSerializer(serializers.ModelSerializer):         #size model serializer
    
    class Meta:
        model = Size
        fields = ['name']

class ProductSerializer(serializers.ModelSerializer):       #Product model serializer
    
    class Meta:
        model = Product
        fields = ['description','name','category']

class ProductImageSerializer(serializers.ModelSerializer):     #Product image serializer

    class Meta:
        model = ProductImage
        fields = ['img_id']

class ProductVariantSerializer(serializers.ModelSerializer):        #Product Varient serializer
    
    class Meta:
        model = ProductVariant
        fields = ['variant_id','product','size','brand','price','img']




class CartItemSerializer(serializers.ModelSerializer):           #CartItem serializer
    product = ProductVariantSerializer()
    sub_total = serializers.SerializerMethodField(method_name="total")
    class Meta:
        model = CartItem
        fields = ["cart","quantity","product","is_active","sub_total"]

    def total(self, cartitems:CartItem):         #subtotal for a single product item 
        return cartitems.quantity * cartitems.product.price


class CartSerializer(serializers.ModelSerializer):     #Cart Serializer
    id            = serializers.IntegerField(read_only=True) 
    user          = serializers.StringRelatedField(source='user.username', read_only=True)  # Use StringRelatedField to get the username  
    items         = CartItemSerializer(many=True,read_only=True)
    total_amount  = serializers.SerializerMethodField(method_name="main_total")   #main_total method to find the total of the cart

    class Meta:
        model    = Cart
        fields   = ["id","user","is_active","items","total_amount"]

    def main_total(self, cart:Cart):   # total amount in a cart
        items    = cart.items.all()
        total    = sum([item.quantity * item.product.price for item in items])    #sum function list comprehension
        return total






class AddtoCartSerializer(serializers.ModelSerializer):
    
    """serializer for add the cart"""

    product_id = serializers.IntegerField()
    

    def save(self, **kwargs):
        cart_id    = self.context["cart_id"]
        product_id = self.validated_data["product_id"]
        quantity = self.validated_data["quantity"]
        
        try:
            cartitem = CartItem.objects.get(product_id=product_id, cart_id=cart_id)
            cartitem.quantity += quantity
            cartitem.save()

            self.instance = cartitem

        except:
            self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data)


        return self.instance

    class Meta:
        model = CartItem
        fields = ['id','product_id','quantity']



class CartUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)

    class Meta:
        model= CartItem
        fiels = ['id','quantity']

















        
# class AddtoCartSerializer(serializers.Serializer):
#     product_id = serializers.IntegerField()
#     quantity = serializers.IntegerField()


#     def validate_product_id(self, value):
#         product = get_object_or_404(ProductVariant, pk=value)
#         return product

#     def create(self, validated_data):
#         user = self.context['request'].user
#         product = validated_data['product_id']
#         quantity = validated_data['quantity']

#         cart, created = Cart.objects.get_or_create(user=user)
#         cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)


        # if not item_created:
        #         cart_item.quantity += quantity
        #         cart_item.save()

        # return cart_item














    




















