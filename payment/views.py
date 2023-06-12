from django.http import JsonResponse
from django.shortcuts import render
from order.models import Order, OrderDetails
from cart.models import Cart
from payment.models import Payment
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json


class PaymentSuccessView(View):
    def post(self, request):
        razorpay_payment_id = request.POST.get("razorpay_payment_id")
        razorpay_order_id = request.POST.get("razorpay_order_id")
        razorpay_signature = request.POST.get("razorpay_signature")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        address = request.POST.get("address")
        cartProducts = Cart.objects.filter(user=request.user)
        if cartProducts:
            order = Order.objects.create(
                user=request.user,
                user_name=f"{first_name} {last_name}",
                address=address,
                razor_pay_order_id=razorpay_order_id,
                mobile=None,
            )
            for cartProduct in cartProducts:
                OrderDetails.objects.create(
                    order=order,
                    product=cartProduct.product,
                    quantity=cartProduct.quantity,
                    price=cartProduct.product.price,
                    variation=cartProduct.variation,
                )
            cartProducts.delete()

        return JsonResponse({"message": "order created"})


@csrf_exempt
def RazorpayWebhook(request):
    requestBody = json.load(request.body.decode("utf-8"))
    print(requestBody)
    payload = requestBody["payload"] 
    if payload["payment"]:
        order_id = payload["payment"]["entity"]["order_id"]
        try:
            order = Order.objects.get(razor_pay_order_id=order_id)
            payment = Payment.objects.get_or_create(order=order)
            payment.payment_id = payload["payment"]["entity"]["id"]
            payment.payment_status = payload["payment"]["entity"]["status"]
            payment.payment_method = payload["payment"]["entity"]["method"]
            payment.created_at = payload["payment"]["entity"]["created_at"]
            payment.amount = payload["payment"]["entity"]["amount"]
            payment.save()
            order.payment_status = True
            order.save()
            return JsonResponse({"message": "Payment Sucessfull"})
        except:
            return JsonResponse({"message": "failed"})
