from django.urls import path
from .views import *

app_name = 'store'

urlpatterns = [
    path('', home),
    path('products_list/', products_list, name='products_list2'),
    path('product_detail/<int:pk>', product_detail, name='product_detail'),
    path('company_list/', company_list, name='company_list'),
    path('company_detail/<int:pk>', company_detail, name='company_detail'),
    path('products_list_category/<slug:category_slug>', products_list, name='product_list_by_category'),

]
