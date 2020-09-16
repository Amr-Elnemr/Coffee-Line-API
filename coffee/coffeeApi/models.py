from django.db import models

# Create your models here.

class Product(models.Model):
    #enumeration objects
    CoffeeType = models.TextChoices('CoffeeType', 'MACHINE POD')
    CoffeeSize = models.TextChoices('CoffeeSize', 'SMALL LARGE ESPRESSO')

    sku = models.CharField(max_length=5, unique=True)
    type = models.CharField(choices=CoffeeType.choices, max_length=10)
    size = models.CharField(choices=CoffeeSize.choices, max_length=10)
    water_line_compatible = models.BooleanField(default=False)
    model = models.CharField(max_length=10, default='')
    pack_size = models.IntegerField(default=0)
    flavor = models.CharField(max_length=20, default='')

