from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    '''Class for managing Product Details'''
    
    CONDITION_TYPE = (
        ("New" , "New"),
        ("Used" , "Used")
    )

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    condition = models.CharField(max_length=100 , choices=CONDITION_TYPE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10 , decimal_places=5)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'product' 
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name 

class ProductImages(models.Model):
    '''Class for managing Product Images'''

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        verbose_name = 'ProductImage' 
        verbose_name_plural = 'ProductImages' 

    def __str__(self):
        return self.product

class Category(models.Model):
    '''Class for managing Product Category'''

    category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/', blank=True, null=True)

    class Meta:
        verbose_name = 'category' 
        verbose_name_plural = 'categories' 

    def __str__(self):
        return self.category_name
    
class Brand(models.Model):
    '''Class for managing Product Brands'''
    
    brand_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'brand' 
        verbose_name_plural = 'brands' 

    def __str__(self):
        return self.brand_name
    