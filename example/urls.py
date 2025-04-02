# example/urls.py
from django.urls import path

from example.views import index, about, contact, products


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('products/', products, name='products'),
    path('contact/', contact, name='contact'),
]
