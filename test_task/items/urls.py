from django.urls import path
from items import views

urlpatterns = [
    path('buy/<int:id>/', views.get_payment_intent, name='get_payment_intent'),
    path('item/<int:id>/', views.item_detail, name='item_detail'),
]