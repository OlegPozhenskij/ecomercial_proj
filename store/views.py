from itertools import product
from django.shortcuts import get_object_or_404, render
from .models import Category, Product

def categories(request):
    return {
        # контекстный процессор, когда данные должены отображаться на всех страницах
        'categories': Category.objects.all()
    }

def all_products(request):
    #получение всех объектов
    products = Product.objects.all()
    #render for loading the templates
    return render(request, 'store/home.html', {'products': products})