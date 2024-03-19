from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse


# Create your views here.

def products_list(request, category_slug=None):
    if category_slug:
        print(category_slug)
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    return render(request, 'store/list.html', {'products': products})


def home(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'store/home.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    context = {
        'product': product
    }
    return render(request, 'store/detail.html', context)


def company_list(request):
    companies = Company.objects.all()
    context = {
        'companies': companies
    }
    return render(request, 'store/company_lst.html', context)


def company_detail(request, pk):
    company = get_object_or_404(Company, id=pk)
    context = {
        'product': company
    }
    return render(request, 'store/company_detail.html', context)
