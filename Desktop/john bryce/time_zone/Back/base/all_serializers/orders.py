from rest_framework import serializers
from base.models import Orders

class Order_serializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        field= ("product_id","order_id","customer_id","order_date")

    def get_all_orders(self,obj):
        res=[]
        for i in obj:
            res.append({
                "order_id": i.order_id,
                "product_id": {
                 "product_id": i.product_id.product_id,   
                 "product_name": i.product_id.product_name,
                 "desc": i.product_id.desc,
                 "image": i.product_id.image.url,
                 "unit": i.product_id.unit,
                 "price": i.product_id.price
                },
                "customer_id":{
                    "customer_id": i.customer_id.customer_id,
                    "customer_name": i.customer_id.customer_name,
                    "address": i.customer_id.address,
                    "city": i.customer_id.city,
                    "country": i.customer_id.country

                },
                
            })   
        return res    

    def get_order_by_id(self,id):
        order = Orders.objects.get(order_id=id)
        return {
              "order_id": order.order_id,
                "product_id": {
                 "product_id": order.product_id.product_id,   
                 "product_name": order.product_id.product_name,
                 "desc": order.product_id.desc,
                 "image": order.product_id.image.url,
                 "unit": order.product_id.unit,
                 "price": order.product_id.price
                },
                "customer_id":{
                    "customer_id": order.customer_id.customer_id,
                    "customer_name": order.customer_id.customer_name,
                    "address": order.customer_id.address,
                    "city": order.customer_id.city,
                    "country": order.customer_id.country

                },
        }   
    
