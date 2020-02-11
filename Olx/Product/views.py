from django.shortcuts import render
from .models import Product

# Create your views here.
def productlist(request):
    productlist = Product.objects.all()
    template = 'Product/product_list.html'
    context = {"product_list":productlist}
    return render(request , template , context)

def productdetail(request, id):
    productdetail = Product.objects.get(id=id)
    template = 'Product/product_detail.html'
    context = {"product_detail":productdetail}
    return render(request , template , context)
