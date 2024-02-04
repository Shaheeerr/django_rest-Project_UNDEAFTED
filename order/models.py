from django.db import models
from register.models import CustomUser,Address
import uuid
from django.utils.functional import cached_property
from home.models import Product
from django.utils.translation import gettext_lazy as _



class Order(models.Model):

    PENDING = "P"
    COMPLETED = "C"


    STATUS_CHOICES = ((PENDING, _("pending")), (COMPLETED, _("completed")))
    
    PAYMENT_COD = "COD"
    PAYMENT_RAZOR_PAY = "RAZOR PAY"

    PAYMENT_CHOICES = [
        (PAYMENT_COD, "Cash On Delivery"),
        (PAYMENT_RAZOR_PAY, "RAZOR PAY Payment")
    ]


    id          = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    customer    = models.ForeignKey('register.CustomUser', on_delete=models.CASCADE, related_name='orders',null=True,blank=True)
    status      = models.CharField(max_length=30, choices=STATUS_CHOICES, default=PENDING)
    payment     = models.CharField(max_length=30, choices=PAYMENT_CHOICES, default=PAYMENT_COD)

    shipping_address = models.ForeignKey(
        Address,
        related_name="shipping_orders",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.customer.username
    
    # @cached_property
    # def total_cost(self):
    #     """
    #     Total cost of all the items in an order
    #     """
    #     return round(sum([order_item.cost for order_item in self.order_items.all()]), 2)




class OrderItem(models.Model):
    order       = models.ForeignKey(Order, related_name="order_items", on_delete=models.CASCADE)
    product     = models.ForeignKey(Product, related_name="product_orders", on_delete=models.CASCADE)
    quantity    = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ("-created_at",)
    
    # @cached_property
    # def cost(self):
    #     """
    #     Total cost of the ordered item
    #     """
    #     return round(self.quantity * self.product.price, 2)