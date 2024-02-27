from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=50)
    state = models.BooleanField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)

