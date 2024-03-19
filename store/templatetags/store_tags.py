from django import template
from ..models import Product
from django.db.models import Count

register = template.Library()


@register.inclusion_tag('partials/new_product.html')
def new_products(count=4):
    products = Product.objects.order_by('-create')[:count]
    return {'products': products}


@register.inclusion_tag('partials/discount_product.html')
def discount_product():
    products = Product.objects.annotate(discount_pro=Count('discount')).order_by('-discount_pro')[:5]
    return {'products': products}


@register.inclusion_tag('partials/best_selling_product.html')
def best_selling_product():
    products = Product.objects.annotate(selling=Count('sold')).order_by('-selling')[:5]
    return {'products': products}


