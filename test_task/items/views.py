from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from items.models import Item
from django.shortcuts import render

@csrf_exempt
def get_payment_intent(request, id):
    item = get_object_or_404(Item, pk=id)
    stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'
    intent = stripe.PaymentIntent.create(
        amount=int(item.price * 100),
        currency='usd',  # Замените 'usd' на вашу фиксированную валюту
        description=item.name,
        payment_method_types=['card'],
    )
    return JsonResponse({'client_secret': intent.client_secret})

def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'item_detail.html', {'item': item})