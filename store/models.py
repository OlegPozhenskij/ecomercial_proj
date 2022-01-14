from distutils.command.upload import upload
from statistics import mode
from tabnanny import verbose
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    #slug - last letters and punctuation of our URL
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    #The related_name attribute specifies the name of the reverse relation from the User model back to your model.
    # -> Category.product.add()
    
    #Продукт будет иметь объекты категории в качестве полей
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, default='admin')
    #blank - При True поле может быть хранить пустое значение
    description = models.TextField(blank=True)
    #we aren't storing images in an DB, we have a link to the image there
    img = models.ImageField(upload_to='images/')

    #   It is Unique! Review later!
    slug = models.SlugField(max_length=250, unique=True)
    
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    # is active to sell
    is_active = models.BooleanField(default=True)
    # auto_now_add=True - happen once
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'products'
        ordering = ('-created', )

    def __str__(self):
        return self.title

