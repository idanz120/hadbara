from django.http import JsonResponse
from rest_framework.decorators import api_view
from base.all_serializers.stores import Stores_serializer
from base.models import Stores

@api_view(['GET','POST','DELETE','PUT'])
def stores(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE":Stores_serializer().get_store_by_id(id),
            },safe=False)
        else: 
            store= Stores.objects.all()
            print(store)
            return JsonResponse({"stores":Stores_serializer().get_all_stores(store)},safe=False) #return array as json response
    if request.method == 'POST': #method post add new row
        store_name =request.data['store_name']
        print(request.data['store_name'])
        Stores.objects.create( store_name= request.data['store_name'],desc= request.data['desc'],image= request.data['image'])
        return JsonResponse({'Added':store_name})

    if request.method == 'DELETE': #method delete a row
        temp= Stores.objects.get(supplier_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Stores.objects.get(supplier_id = id)
        temp.store_name =request.data['store_name']
        temp.save()
        return JsonResponse({'PUT': id})

@api_view(['GET'])
def get_stoer_by_name(request,name):
    store =request.data['store_name']
    print(request.data['store_name'])
    storename= Stores.objects.get(store_name=name)
    print(storename)
    return JsonResponse({'HERE':Stores_serializer().get_store_by_name(storename)},safe=False)   

