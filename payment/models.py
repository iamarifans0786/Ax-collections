from django.db import models
from order.models import Order


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    payment_id = models.CharField(max_length=255, null=True, blank=True)
    payment_status = models.CharField(max_length=255, null=True, blank=True)
    payment_method = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.CharField(max_length=255, null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
 
    
    def __str__(self):
        return str(self.payment_id)
