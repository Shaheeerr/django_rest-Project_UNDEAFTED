from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem
from .serializers import OrderSerializer,CreateOrderSerilizer
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet


class OrderViewSet(ModelViewSet):   #Get User Order
    # permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset=Order.objects.all()

    def get_serializer_class(self):
        if self.request.method=="POST":
            return CreateOrderSerilizer
        return OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return  Order.objects.filter(customer=user)





# class OrderViewSet(viewsets.ModelViewSet):
#     # permission_classes = [IsAuthenticated]

#     def get_serializer_class(self):
#         if self.request.method=="POST":
#             return CreateOrderSerilizer
#         return OrderSerializer
    
#     def get_queryset(self):
#         user = self.request.user
#         if user.is_staff:
#             return Order.objects.get()
#         return  Order.objects.filter(customer=user)

#     def get_serializer_context(self):
#         return super().get_serializer_context()













# class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]

# class OrderItemCreateView(generics.CreateAPIView):
#     queryset = OrderItem.objects.all()
#     serializer_class = OrderItemSerializer
#     permission_classes = [IsAuthenticated]

# class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = OrderItem.objects.all()
#     serializer_class = OrderItemSerializer
#     permission_classes = [IsAuthenticated]
