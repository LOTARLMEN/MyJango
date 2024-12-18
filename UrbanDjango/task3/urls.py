from django.urls import path
from .views import  *

urlpatterns = [
    path('', main, name='main'),
    path('store/', store, name='store'),
    path('cart/', cart, name='cart'),
]