from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from base.all_serializers.supplier import Suppliers_serializer
from base.models import Supplier
from rest_framework.permissions import IsAuthenticated



@api_view(['GET','POST','DELETE','PUT'])
@permission_classes([IsAuthenticated])
def suppliers(request,id=-1):
    if request.method == 'GET':#method get all and single
        print(request)
        if int(id) > -1: #get single product
            return JsonResponse({
            "SINGLE":Suppliers_serializer().get_supplier_by_id(id),
            },safe=False)
        else: 
            sup= Supplier.objects.all()
            print(sup)
            return JsonResponse({"suppliers":Suppliers_serializer().get_all_suppliers(sup)},safe=False) #return array as json response
    if request.method == 'POST': #method post add new row
        supplier_name =request.data['supplier_name']
        print(request.data['supplier_name'])
        Supplier.objects.create( supplier_name = request.data['supplier_name'],address= request.data['address'],city= request.data['city'],postal_code= request.data['postal_code'],country= request.data['country'],phone= request.data['phone'])
        return JsonResponse({'Added':supplier_name})

    if request.method == 'DELETE': #method delete a row
        temp= Supplier.objects.get(supplier_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})

    if request.method == 'PUT': #method delete a row
        temp=Supplier.objects.get(supplier_id = id)
        temp.supplier_name =request.data['supplier_name']
        temp.save()
        return JsonResponse({'PUT': id})