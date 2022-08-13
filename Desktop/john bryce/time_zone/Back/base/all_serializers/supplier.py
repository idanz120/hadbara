from rest_framework import serializers
from base.models import Supplier

class Suppliers_serializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        field= ("supplier_id","supplier_name","address","city","postal_code","country","phone")

    def get_all_suppliers(self,obj):
        res=[]
        for i in obj:
            res.append({
                "id":i.supplier_id,
                "supplier_name":i.supplier_name,
                "address":i.address,
                "city":i.city,
                "postal_code":i.postal_code,
                "country":i.country,
                "phone":i.phone
            })    
        return res    

    def get_supplier_by_id(self,id):
        sup = Supplier.objects.get(supplier_id=id)
        return {
            "id": sup.supplier_id,
            "supplier_name": sup.supplier_name,
            "address": sup.address,
            "city": sup.city,
            "postal_code":sup.postal_code,
            "country":sup.country,
            "phone":sup.phone
        }   
    
