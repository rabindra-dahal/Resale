from django.shortcuts import render

# Create your views here.

def profile(request):
    '''Profile Views'''
    template = 'registration/profile.html'
    # context = {"product_detail":product_details, 'product_images':product_images}
    return render(request, template)

