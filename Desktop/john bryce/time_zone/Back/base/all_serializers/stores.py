from rest_framework import serializers
from base.models import Stores

class Stores_serializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        field= ("supplier_id","store_name","desc","image")

    def get_all_stores(self,obj):
        res=[]
        for i in obj:
            res.append({
                "supplier_id":{
                  "supplier_id":i.supplier_id.supplier_id,
                  "supplier_name":i.supplier_id.supplier_name,
                  "phone":i.supplier_id.phone,
                  },
                  "store_name":i.store_name,
                  "desc":i.desc,
                  "image":i.image.url,
            })   
        return res    

    def get_store_by_id(self,id):
        store = Stores.objects.get(supplier_id=id)
        return {
           "supplier_id":{
                  "supplier_id":store.supplier_id.supplier_id,
                  "supplier_name":store.supplier_id.supplier_name,
                  "phone":store.supplier_id.phone,
                  },
                  "store_name":store.store_name,
                  "desc":store.desc,
                  "image":store.image.url,
        }   
    
    def get_store_by_name(self,name):
            try:
                store = Stores.objects.get(store_name = name)
            except:return {"Not" :"Found"}    
            print(store)
            return{
                    "store_name":store.store_name,
                    "desc":store.desc,
                    }    
