from ..models import *
import sys,inspect



def insertProduct(self,request,format=None):
    
    Product,created = Product.objects.get_or_create(ProductName=request['ProductName'])
    Product.ProductPrice = request['ProductPrice']
    Product.save()