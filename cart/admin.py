from django.contrib import admin
from cart.models import Cart

@admin.register(Cart)
class cartAdmin(admin.ModelAdmin):
   list_display=['user','product','variation','quantity']
   list_filter=['user']
   search_fields=['user']
  