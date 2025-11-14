from django.shortcuts import render,redirect
from product.models import Product
from django.contrib import messages
from .models import Cart
from django.contrib.auth.decorators import login_required


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

@login_required
def add_to_cart(request,product_id):
    user = request.user
    product = Product.objects.get(pk = product_id)
    check_product_presence = Cart.objects.filter(user =user, product = product)
    if check_product_presence:
        messages.add_message(request,messages.ERROR,"Product is already in cart")
        return redirect("home-page")
    else:
        cart = Cart.objects.create(product=product, user = user)
        if cart:
            messages.add_message(request,messages.SUCCESS,"Product added to cart")
            return redirect("all-cart-items")
        else:
            messages.add_message(request, messages.ERROR, "Unable to add item to the cart")

def show_cart_items(request):
    user=request.user
    cart_items=Cart.objects.filter(user=user)
    return render(request,"userpage/cart-items.html",{
        'cart':cart_items,
        'totalitems':len(cart_items)>0
    })