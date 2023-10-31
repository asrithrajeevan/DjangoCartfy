from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.user_registration, name='register'),
    path('add-product', views.add_product, name='add-product'),         
    path('update-product', views.update_product, name='update-product'),
    path('delete-product', views.delete_product, name='delete-product'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart_view', views.cart_view, name='cart_view'),
    path('remove_item_from_cart/<int:product_id>/', views.remove_item_from_cart, name='remove_item_from_cart'),
]

# we use the builtin login form in django
# http://127.0.0.1:8000/accounts/login/