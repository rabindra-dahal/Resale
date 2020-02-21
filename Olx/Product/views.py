from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Count, Q
from .models import Product, ProductImages, Category

# Create your views here.
def productlist(request, category_slug=None):
    '''Product List Views'''
    category = None
    product_lists = Product.objects.all()
    category_lists = Category.objects.annotate(total_products=Count('product'))

    if category_slug:
        category = Category.objects.get(slug=category_slug)
        product_lists = product_lists.filter(category=category)
        
    search_query = request.POST.get("q")
    if search_query:
        product_lists = product_lists.filter(
            Q(name__icontains=search_query)|Q(description__icontains=search_query)|Q(condition__icontains=search_query)|Q(brand__brand_name__icontains=search_query))
    # Code for pagination starts
    paginator = Paginator(product_lists, 2)
    page = request.GET.get('page')
    product_lists = paginator.get_page(page)
    # End of pagination
    template = 'Product/product_list.html'
    context = {"product_list":product_lists, "category_list":category_lists, "category":category}
    return render(request, template, context)

def productdetail(request, product_slug):
    '''Product Details Views'''
    product_details = Product.objects.get(slug=product_slug)
    product_images = ProductImages.objects.filter(product=product_details)
    template = 'Product/product_detail.html'
    context = {"product_detail":product_details, 'product_images':product_images}
    return render(request, template, context)
