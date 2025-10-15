from django.shortcuts import render,redirect
from .models import Product,Category



def get_all_product(request):
    products=Product.objects.all()
    return render(request, "product/product_list.html",{'products':products})



def category_list(request):
    categories = Category.objects.all()
    return render(request, 'product/category_list.html', {'categories': categories})

def delete_product(request, product_id):
    product=Product.objects.get(id=product_id)
    product.delete()
    return redirect("product_list")


def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('category_list')  




