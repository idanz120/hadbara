from django.http import JsonResponse
from rest_framework.decorators import api_view
from base.all_serializers.product import Products_serializer
from base.models import Products
from base.models import Customers
from django.contrib.auth.models import User

@api_view(['GET','POST','DELETE','PUT'])
def products(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE":Products_serializer().get_product_by_id(id),
            },safe=False)
        else: 
            prod= Products.objects.all()
            print(prod)
            return JsonResponse({"products":Products_serializer().get_all_products(prod)},safe=False) #return array as json response
    if request.method == 'POST': #method post add new row
        product_name =request.data['product_name']
        print(request.data['product_name'])
        Products.objects.create( product_name= request.data['product_name'],desc= request.data['desc'],image= request.data['image'],unit= request.data['unit'],price = request.data['price'])
        return JsonResponse({'Added':product_name})

    if request.method == 'DELETE': #method delete a row
        temp= Products.objects.get(product_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Products.objects.get(product_id = id)
        temp.product_name =request.data['product_name']
        temp.save()
        return JsonResponse({'PUT': id})

@api_view(['GET'])
def get_product_by_name(request,name):
        #prod =request.data['product_name']
        #print(prod)
        try:
            prod_name= Products.objects.get(product_name=name)
        except:return JsonResponse({"Not" :"Found"}) 
        print(prod_name)
        return JsonResponse({'HERE':Products_serializer().get_product_by_name(prod_name)},safe=False)   

