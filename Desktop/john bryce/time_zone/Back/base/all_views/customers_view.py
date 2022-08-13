from django.http import JsonResponse
from rest_framework.decorators import api_view
from base.all_serializers.customers import Customers_serializer
from base.models import Customers
from django.contrib.auth.models import User

@api_view(['GET','POST','DELETE','PUT'])
def customers(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE":Customers_serializer().get_customer_by_id(id),
            },safe=False)
        else: 
            cus= Customers.objects.all()
            print(cus)
            return JsonResponse({"Customers":Customers_serializer().get_all_customers(cus)},safe=False) #return array as json response
    if request.method == 'POST': #method post add new row
        customer_name =request.data['customer_name']
        print(request.data['customer_name'])
        # Create New Customer
        Customers.objects.create( address= request.data['address'],city= request.data['city'],postal_code= request.data['postal_code'],country= request.data['country'],customer_name = request.data['customer_name'])
        # Create New User//TEST
        User.objects.create_user(username= request.data['customer_name'],
                             email=request.data['email'],
                             password= request.data['password'])
        return JsonResponse({'Added':customer_name})

    if request.method == 'DELETE': #method delete a row
        temp= Customers.objects.get(customer_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Customers.objects.get(customer_id = id)
        temp.customer_name =request.data['customer_name']
        temp.save()
        return JsonResponse({'PUT': id})