
from django.urls import path
from .views import order_list, order

urlpatterns = [
    path('orders/', order_list, name='order_list'),
    path('orders/new', order, name='order'),
]