from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
import datetime
import os
# Create your models here.

class Supplier(models.Model):
       supplier_id = models.AutoField(primary_key=True,editable=False) 
       supplier_name =   models.CharField(max_length=20,null=True,blank=True)
       address=models.CharField(max_length=20,null=True,blank=True)
       city=models.CharField(max_length=20,null=True,blank=True)
       postal_code= models.IntegerField(null=True,blank=True)
       country=models.CharField(max_length=20,null=True,blank=True)
       phone=models.CharField(max_length=12,null=True,blank=True)
    
       def __str__(self):
     	    return self.supplier_name

class Customers(models.Model):
    customer_id =models.AutoField(primary_key=True,editable=False) 
    address = models.CharField(max_length=50,null=True,blank=True)
    city=models.CharField(max_length=20,null=True,blank=True)
    postal_code= models.IntegerField(null=True,blank=True)
    country=models.CharField(max_length=20,null=True,blank=True)
    customer_name=models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
     	    return self.customer_name



def filepath(request,filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow,old_filename)
    return os.path.join('uploads/',filename)


class Stores(models.Model):
   #store_id=  models.AutoField(primary_key=True,editable=False)
   supplier_id =models.OneToOneField(Supplier,on_delete=models.CASCADE,primary_key=True, )
   store_name=models.CharField(max_length=20,null=True,blank=True)
   desc=models.TextField()
   image =models.ImageField(upload_to=filepath,null=True,blank=True)
   
   
   def __str__(self):
     	return self.store_name

class Products(models.Model):
     store_id=models.ForeignKey(Stores,on_delete=models.SET_NULL,null=True)
     product_id =models.AutoField(primary_key=True,editable=False) 
     product_name=models.CharField(max_length=20,null=True,blank=True)
     desc= models.TextField()
     image =models.ImageField(null=True,blank=True,default='/placeholder.png')
     unit =models.IntegerField(null=True,blank=True)
     price=models.IntegerField(null=True,blank=True)
    
     def __str__(self):
     	return self.product_name

class Orders(models.Model):
     product_id=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
     order_id = models.AutoField(primary_key=True,editable=False)   
     customer_id = models.ForeignKey(Customers,on_delete=models.SET_NULL,null=True)
     order_date =models.DateTimeField(auto_now_add=True)            

class Order_Details(models.Model):
    order_detail_id =models.AutoField(primary_key=True,editable=False)
    order_id =models.ForeignKey(Orders,on_delete=models.SET_NULL,null=True)
    product_id=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(null=True,blank=True)
            
