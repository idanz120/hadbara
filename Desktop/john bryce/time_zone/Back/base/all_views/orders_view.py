from django.http import JsonResponse
from rest_framework.decorators import api_view
from base.models import Orders
from base.all_serializers.orders import Order_serializer
from base.models import Stores

@api_view(['GET','POST','DELETE','PUT'])
def orders(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE":Order_serializer().get_order_by_id(id),
            },safe=False)
        else: 
            order= Orders.objects.all()
            print(order)
            return JsonResponse({"orders":Order_serializer().get_all_orders(order)},safe=False) #return array as json response
    #if request.method == 'POST': #method post add new row
    #    order_date =request.data['order_date']
    #    print(request.data['order_date'])
    #    Orders.objects.create( order_date= request.data['order_date'])
    #    return JsonResponse({'Added':order_date})

    if request.method == 'DELETE': #method delete a row
        temp= Orders.objects.get(order_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

   # if request.method == 'PUT': #method delete a row
   #    temp=Orders.objects.get(order_id = id)
   #     temp.order_date =request.data['order_date']
   #    temp.save()
   #   return JsonResponse({'PUT': id})