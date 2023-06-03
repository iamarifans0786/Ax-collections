from django.db import models
from django.contrib.auth.models import User
from product.models import Product, ProductVariation


class Order(models.Model):
    STATUS_CHOICE = (
        ("Pending", "Pending"),
        ("inprogress", "inprogress"),
        ("Dispatch", "Dispatch"),
        ("Delivered", "Delivered"),
        ("Canceled", "Canceled"),
        ("Rejected", "Rejected"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True)
    address = models.TextField()
    mobile = models.CharField(max_length=12)
    payment_status = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default="Pending")

    def __str__(self):
        return f"{str(self.id)} {self.user}" 


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    variation = models.ForeignKey(
        ProductVariation, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f"{str(self.order.id)} {self.product}"

    class Meta:
        verbose_name = "Order Detail"
