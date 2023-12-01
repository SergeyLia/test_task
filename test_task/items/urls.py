from django.urls import path
from items.views import BuyItemView, ItemDetailView

app_name = 'items'

urlpatterns = [
    path('buy/<int:item_id>/', BuyItemView.as_view(), name='buy_item'),
    path('item/<int:item_id>/', ItemDetailView.as_view(), name='item_detail'),
]