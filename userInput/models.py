from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    description = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self): 
        return self.description