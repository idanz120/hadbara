from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(x):
   return JsonResponse('hello', safe=False)


