from django.urls import path

from .views import add_to_cart, cart, remove_from_cart, clear_cart

urlpatterns = [
    path('carts/', cart, name= 'cart'),
    path('carts/add/<product_id>', add_to_cart, name= 'add_to_cart'),
    path('carts/remove_from_cart/<product_id>', remove_from_cart, name= 'remove_from_cart'),
    path('carts/clear_cart/', clear_cart, name= 'clear_cart'),

   ]