from django.contrib import admin
from django.urls import path,include
from . import views
from base.all_views import supplier_view
from base.all_views import customers_view
from base.all_views import products_view
from base.all_views import stores_view
from base.all_views import orders_view
from base.all_views import order_details_view
from base .all_views import user_view
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from base.all_views._token_view import MyTokenObtainPairView
from . import views
from .all_views import _token_view

urlpatterns = [
    path('', views.index),
    path('suppliers/', supplier_view.suppliers),
    path('suppliers/<id>', supplier_view.suppliers),
    path('customers/', customers_view.customers),
    path('customers/<id>', customers_view.customers),
    path('products/', products_view.products),
    #Test
    path('product_by_name/<name>', products_view.get_product_by_name),
    path('products/<id>', products_view.products),
    path('stores/', stores_view.stores),
    path('stores/<id>', stores_view.stores),
    path('stoer_by_name/<name>', stores_view.get_stoer_by_name),
    path('orders/', orders_view.orders),
    path('orders/<id>', orders_view.orders),
    path('order_details/', order_details_view.order_details),
    path('order_details/<id>', order_details_view.order_details),
    path('users/', user_view.users),
    path('users/<id>', user_view.users),
    path('user_by_name/<name>', user_view.user_by_name),
    # Login
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
