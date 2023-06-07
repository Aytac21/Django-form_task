from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField( blank = True,null=True)

    def __str__(self):
        return self.name