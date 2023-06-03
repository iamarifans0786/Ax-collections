from django.contrib import admin, messages
from order.models import Order, OrderDetails


""" for updation os ststus fields on admin pannel """


def active_status(modelAdmin, request, queryset):
    try:
        queryset.update(payment_status=True)
        messages.success(request, "Selected record(s) marked as active")
    except Exception as e:
        messages.error(request, str(e))


def inactive_status(modelAdmin, request, queryset):
    try:
        queryset.update(payment_status=False)
        messages.success(request, "Selected record(s) marked as inactive")
    except Exception as e:
        messages.error(request, str(e))


""" for the saprate column in Order for OrderDetails """


class OrderDetailsInline(admin.StackedInline):
    model = OrderDetails


@admin.register(Order)
class orderAdmin(admin.ModelAdmin):
    list_display = ["user", "address", "mobile", "payment_status", "status"]
    list_filter = ["user__username"]
    search_fields = ["user"]
    date_hierarchy = "date_time"
    actions = (active_status, inactive_status)
    inlines = (OrderDetailsInline,)


# @admin.register(OrderDetails)
# class orderDetailsAdmin(admin.ModelAdmin):
#     list_display = ["order", "product", "quantity", "price"]
#     list_filter = ["product"]
#     search_fields = ["product"]
