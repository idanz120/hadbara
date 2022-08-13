from rest_framework import serializers
from base.models import Customers

class Customers_serializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        field= ("customer_id","address","city","postal_code","country","customer_name")

    def get_all_customers(self,obj):
        res=[]
        for i in obj:
            res.append({
                "id":i.customer_id,
                "address":i.address,
                "city":i.city,
                "postal_code":i.postal_code,
                "country":i.country,
                "customer_name":i.customer_name
            })    
        return res    

    def get_customer_by_id(self,id):
        cus = Customers.objects.get(customer_id=id)
        return {
            "id": cus.customer_id,
            "address": cus.address,
            "city": cus.city,
            "postal_code":cus.postal_code,
            "country":cus.country,
            "customer_name":cus.customer_name
        }   
    
