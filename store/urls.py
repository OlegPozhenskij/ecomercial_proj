from django.urls import path

from . import views

# для связки с urls из core -
# если поменять ничего не сломается
app_name = 'store'

urlpatterns = [
    path('', views.all_products, name="all_products"),
    # slug1 - type of data, our_slug - name of the var, where we want to store the data and send to views!
    # прописываем только slug продукта - он присв
    path('item/<slug:our_slug>/', views.product_details, name="product_details")
]

