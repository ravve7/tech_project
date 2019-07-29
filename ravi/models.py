from django.db import models


# Create your models here.
class Products(models.Model):
    product_name= models.CharField(max_length = 15, unique=True)
    def __str__(self):
        return self.product_name

class inventory(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    inventory_level=models.IntegerField()
    products = models.ForeignKey(Products, on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     self.revision += 1
    #     return super(ClassificationLabel, self).save()
