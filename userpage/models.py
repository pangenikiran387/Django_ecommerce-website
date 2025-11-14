
from django.db import models
from product.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.user} => {self.product}"




  


