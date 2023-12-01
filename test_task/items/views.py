from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
import stripe

from items.models import Item

stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'

class BuyItemView(View):
    def get(self, request, item_id):
        item = get_object_or_404(Item, pk=item_id)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://example.com/success/',
            cancel_url='http://example.com/cancel/',
        )
        return JsonResponse({'session_id': session.id})

class ItemDetailView(View):
    def get(self, request, item_id):
        item = get_object_or_404(Item, pk=item_id)
        return render(request, 'item_detail.html', {
            'name': item.name,
            'description': item.description,
            'price': item.price,
            'item_id': item_id,
        })