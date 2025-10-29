from django.shortcuts import render
from product.models import Product

def home_page(request):
    products = Product.objects.all()[:6]
    return render(request,"userpage/homepage.html",{
        'products': products
    })


def product_detail(request, pk):
    products=Product.objects.get(pk=pk)
    return render(request,"userpage/product_detail.html",{
        'product':products
    })
