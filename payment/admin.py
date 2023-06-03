from django.contrib import admin
from payment.models import Payment

@admin.register(Payment)
class payment(admin.ModelAdmin):
    list_display = ["order", "transaction_id","status"]
    list_filter = ["order"]
    search_fields = ["order"]

