from django.contrib import admin
from .models import Category, Product

# Register your models here.

# admin.site.register(Category, Product) - если мы не хоти менять отображение!

#добавляем модель в отображение панели Admin
@admin.register(Category) #на основе класса Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    #автозаполняемое поле, генерирующее slug на английском, на основе имени категории
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price',
                    'in_stock', 'created', 'updated',]
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}

