
from django.db import models


class category(models.Model):
    category_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category=models.ForeignKey(to=category, on_delete=models.CASCADE)
    product_price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_images')
    is_instock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.product_name