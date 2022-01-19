from django.contrib.auth.models import User
from django.db import models
#allow us to build an url
from django.urls import reverse


# class ProductManager(models.Manager):
#     def get_queryset(self):
#         return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
     #slug - last letters and punctuation of our URL
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    # def get_absolute_url(self):
    #     return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
     #The related_name attribute specifies the name of the reverse relation from the User model back to your model.
    # -> Category.product.add()
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    #blank - При True поле может быть хранить пустое значение
    description = models.TextField(blank=True)
     #we aren't storing images in an DB, we have a link to the image there
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
     # is active to sell
    is_active = models.BooleanField(default=True)
     # auto_now_add=True - happen once
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # objects = models.Manager()
    # products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_details', args=[self.slug])

    def __str__(self):
        return self.title
