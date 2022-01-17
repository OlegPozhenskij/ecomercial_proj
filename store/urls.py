from django.urls import path

from . import views

# для связки с urls из core -
# если поменять ничего не сломается
app_name = 'store'

urlpatterns = [
    path('', views.all_products, name="all_products")
]

