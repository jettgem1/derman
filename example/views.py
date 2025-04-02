# example/views.py
from django.shortcuts import render
from datetime import datetime


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
        return render(request, 'contact.html')


def products(request):
    return render(request, 'products.html')
