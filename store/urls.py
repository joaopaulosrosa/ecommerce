from django.urls import path
from . import views

urlpatterns = [

    path('', views.store, name='store'),
    path('product/<str:pk>', views.product, name='product'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout')

]
