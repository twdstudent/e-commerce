from django.shortcuts import render
from products.models import Product

# Create your views here.

def do_search(request):
    products = Product.object.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products":products})
    
    
"""
But first, we have to import the model product from products.models.
So we create a method called do_search().
We have the model called Product.objects.filter.
And filter is a built-in function.
And we have (name_icontains=request.GET['q]), and this will get whatever 'q' is 
returned from the form, so we'll give the form a name of 'q'.
And whatever you type into that form will then be used to filter the products.
"""