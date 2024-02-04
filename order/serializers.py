from rest_framework import serializers
from .models import Order, OrderItem
from home.models import *
class OrderItemSerializer(serializers.ModelSerializer):    #serializer for OrderItem
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'order']




class OrderSerializer(serializers.ModelSerializer):    #serializer for Order
    items = OrderItemSerializer(many=True,read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'customer', 'status', 'shipping_address', 'status','items']





class CreateOrderSerilizer(serializers.Serializer):       #serializer for Create a Order
    cart_id = serializers.CharField()                     

    def save(self, **kwargs):
        cart_id = self.validated_data["cart_id"]
        user_id = self.context["user_id"]
        order = Order.objects.create(customer_id=user_id)
        print(cart_id)
        return order





    





# class OrderItemSerializer(serializers.ModelSerializer):
#     product = ProductSerializer()  # Assuming you have a ProductSerializer

#     class Meta:
#         model = OrderItem
#         fields = ['id', 'product', 'quantity']