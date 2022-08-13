from django.http import JsonResponse
from rest_framework.decorators import api_view
from base.models import Order_Details
from base.all_serializers.order_details import Order_Details_serializer
from base.models import Orders

@api_view(['GET','POST','DELETE','PUT'])
def order_details(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE":Order_Details_serializer().get_order_details_by_id(id),
            },safe=False)
        else: 
            details= Order_Details.objects.all()
            print(details)
            return JsonResponse({"orders":Order_Details_serializer().get_all_orders_details(details)},safe=False) #return array as json response
    if request.method == 'POST': #method post add new row
        quantity =request.data['quantity']
        print(request.data['quantity'])
        Order_Details.objects.create( quantity= request.data['quantity'])
        return JsonResponse({'Added_quantity':quantity})

    if request.method == 'DELETE': #method delete a row
        temp= Order_Details.objects.get(order_detail_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
       temp=Order_Details.objects.get(order_detail_id = id)
       temp.quantity =request.data['quantity']
       temp.save()
       return JsonResponse({'PUT': id})