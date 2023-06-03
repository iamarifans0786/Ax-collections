from django.db import models
from order.models import Order


class Payment(models.Model):
    STATUS_CHOICE = (
        ("Successfull", "Successfull"),
        ("Pending", "Pending"),
        ("Processing", "Processing"),
        ("Failed", "Failed"),
    )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    transaction_id = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE)
    
    def __str__(self):
        return self.transaction_id
