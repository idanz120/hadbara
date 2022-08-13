from rest_framework import serializers
from base.models import Products
from django.http import JsonResponse

class Products_serializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        field= ("store_id","product_id","product_name","desc","image","unit","price")

    def get_all_products(self,obj):
        res=[]
        for i in obj:
            res.append({
                "store_id":{
                  "store_name":i.store_id.store_name,
                  "desc":i.store_id.desc,
                  "image":str(i.store_id.image),
                  },
                  "product_id":i.product_id,
                  "product_name":i.product_name,
                  "desc":i.desc,
                  "image":i.image.url,
                  "unit":i.unit,
                  "price":i.price
            })   
        return res    

    def get_product_by_id(self,id):
        prod = Products.objects.get(product_id=id)
        return {
             "store_id":{
                  "store_name":prod.store_id.store_name,
                  "desc":prod.store_id.desc,
                  "image":str(prod.store_id.image),
                  },
            "product_id": prod.product_id,
            "product_name": prod.product_name,
            "desc":prod.desc,
            "image":prod.image.url,
            "unit":prod.unit,
            "price":prod.price
        }   
    
    def get_product_by_name(self,name):
            prod = Products.objects.get(product_name = name)
            print(prod)
            return {
                    "product_id":prod.product_id,
                    "product_name":prod.product_name,
                    "desc":prod.desc,
                    "image":prod.image.url,
                    "unit":prod.unit,
                    "price":prod.price,
                    "store_id":{
                        "store_name":prod.store_id.store_name,
                        "desc":prod.store_id.desc,
                        "image":str(prod.store_id.image)
                    }
                    }    
              
           