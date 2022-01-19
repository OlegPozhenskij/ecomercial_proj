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

def product_details(request, our_slug):
    product = get_object_or_404(Product, slug=our_slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})
    
def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'products': products,'category': category})