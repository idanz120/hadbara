from rest_framework import serializers
from base.models import Order_Details

class Order_Details_serializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Details
        field= ("order_detail_id","order_id","product_id","quantity")

    def get_all_orders_details(self,obj):
        res=[]
        for i in obj:
            res.append({
                        "order_detail_id":i.order_detail_id,
                    "order_id":{
                        "order_id":i.order_id.order_id,
                        "customer_id":i.order_id.customer_id.customer_id,
                        "address":i.order_id.customer_id.address,
                        "city":i.order_id.customer_id.city,
                        "postal_code":i.order_id.customer_id.postal_code,
                        "country":i.order_id.customer_id.country,
                        "customer_name":i.order_id.customer_id.customer_name,
                    },
                    "product_id": {
                        "product_id": i.product_id.product_id,   
                        "product_name": i.product_id.product_name,
                        "desc": i.product_id.desc,
                        "image": i.product_id.image.url,
                        "unit": i.product_id.unit,
                        "price": i.product_id.price
                        },
                        "quantity":i.quantity
                
            })   
        return res    

    def get_order_details_by_id(self,id):
        details = Order_Details.objects.get(order_detail_id=id)
        return {
              "order_detail_id":details.order_detail_id,
                    "order_id":{
                        "order_id":details.order_id.order_id,
                        "customer_id":details.order_id.customer_id.customer_id,
                        "address":details.order_id.customer_id.address,
                        "city":details.order_id.customer_id.city,
                        "postal_code":details.order_id.customer_id.postal_code,
                        "country":details.order_id.customer_id.country,
                        "customer_name":details.order_id.customer_id.customer_name,
                    },
                    "product_id": {
                        "product_id": details.product_id.product_id,   
                        "product_name": details.product_id.product_name,
                        "desc": details.product_id.desc,
                        "image": details.product_id.image.url,
                        "unit": details.product_id.unit,
                        "price": details.product_id.price
                        },
                        "quantity":details.quantity
        }   