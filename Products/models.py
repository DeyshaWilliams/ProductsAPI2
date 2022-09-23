from django.db import models

# Create your models here.
class Product(models.Model):
    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
