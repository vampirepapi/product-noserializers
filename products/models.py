from django.db import models

# Create your models here.
class ProductItem(models.Model):
    ProductId = models.AutoField(primary_key=True)  # It is an auto field.
    ProductName = models.CharField(max_length=50, blank=True, null=True)
    ProductPrice = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.ProductName)