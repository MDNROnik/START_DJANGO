from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# /products for this funciton
# uniform resource locator(address)
def index(request):
    products = Product.objects.all()
    return render(
        request,
        'index.html',
        {
            'products':products
        }
    )

def index2(request):
    return HttpResponse("Hello Fucking World 2")
