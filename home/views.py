from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import CategorySerializer,BrandSerializer,SizeSerializer,ProductSerializer,ProductImageSerializer,ProductVariantSerializer,CartItemSerializer,CartSerializer,AddtoCartSerializer
from rest_framework.views import APIView
from rest_framework import generics, permissions, status, mixins
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from urllib import response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication






class CategoryViewSet(ModelViewSet): 

    """Catergory View"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer




class BrandViewSet(ModelViewSet):

    """BrandView"""

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class SizeViewSet(ModelViewSet):

    """Size View Set"""

    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class ProductViewSet(ModelViewSet):

    """ProductView"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]       # djangofilter for search,ordering,filter
    filterset_fields = ['category_id']
    search_fields = ['name','description']
    ordering_fields = ['name']




class ProductImageViewSet(ModelViewSet):

    """Product image View"""

    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductVariantViewSet(ModelViewSet):

    """ProductVariantView"""

    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer




class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):

    """Cart View Set."""

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated] 


class CartItemViewSet(ModelViewSet):

    """Cart Item View"""
    
    def get_queryset(self):    # Overrides the get_queryset method of the viewset
        return CartItem.objects.filter(cart_id=self.kwargs["cart_pk"])   
     

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddtoCartSerializer
        
        elif self.request.method == "PATCH":
            return UpdateCartItemSerializer
        
        return CartItemSerializer

    def get_serializer_context(self):    # method ensures that the serializer has access to the cart_id from the URL pattern
        return {"cart_id": self.kwargs["cart_pk"]}
  
















# class CartItemCreateView(mixins.ListModelMixin, viewsets.GenericViewSet):
#     serializer_class = AddtoCartSerializer
#     # permission_classes = [permissions.IsAuthenticated]
#     queryset = CartItem.objects.all()
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status=status.HTTP_201_CREATED)




# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# class CartItemReteriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

#      serializer_class = CartItemSerializer
#      queryset         = CartItem.objects.all()
#      lookup_field     = 'pk'     

#      """

#             getinging  the cartitem updating the
#             using put 
#      """

     




