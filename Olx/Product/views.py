from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product, ProductImages

# Create your views here.
def productlist(request):
    '''Product List Views'''
    product_lists = Product.objects.all()
    template = 'Product/product_list.html'
    # Code for pagination starts
    paginator = Paginator(product_lists, 2)
    page = request.GET.get('page')
    product_lists = paginator.get_page(page)
    # End of pagination
    context = {"product_list":product_lists}
    return render(request, template, context)

def productdetail(request, product_slug):
    '''Product Details Views'''
    product_details = Product.objects.get(slug=product_slug)
    product_images = ProductImages.objects.filter(product=product_details)
    template = 'Product/product_detail.html'
    context = {"product_detail":product_details, 'product_images':product_images}
    return render(request, template, context)
