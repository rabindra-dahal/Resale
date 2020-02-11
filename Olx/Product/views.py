from django.shortcuts import render
from .models import Product

# Create your views here.
def productlist(request):
    '''Product List Views'''
    productlist = Product.objects.all()
    template = 'Product/product_list.html'
    context = {"product_list":productlist}
    return render(request, template, context)

def productdetail(request, product_slug):
    '''Product Details Views'''
    productdetail = Product.objects.get(slug=product_slug)
    template = 'Product/product_detail.html'
    context = {"product_detail":productdetail}
    return render(request, template, context)
