from django.urls import path
from . import views


urlpatterns = [
path("add-to-cart/",views.AddToCartView.as_view(),name='AddToCartView'),
path("my-cart/",views.MyCartView.as_view(),name='MyCartView'),
path("remove-cart-item/<int:cart_id>",views.RemoveCartItem.as_view(),name='RemoveCartItem'),
path("checkout",views.CheckoutView.as_view(),name='CheckoutView'),
]
