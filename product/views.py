from django.shortcuts import render,redirect
from .models import Product,Category
from .forms import Categoryform,Productform



# def get_all_product(request):
#     products=Product.objects.all()
#     return render(request, 'product/product_list.html',{'products':products})


def  get_all_product(request):
    products = Product.objects.all() 
    return render(request, 'product/product_list.html', {'products': products})




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

def add_category(request):
    return render(request, "product/add_category.html", {'form':Categoryform})



#post 
def add_category(request):
    if request.method=="POST":
        form=Categoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category_list")
        
        else:
            return render(request, "product/add_category.html",{'form':form})
    
    return render(request,"product/add_category.html", {"form":Categoryform})

def update_category(request,category_id):
    category=Category.objects.get(id=category_id)
    if request.method=="POST":
        form=Categoryform(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("category_list")
        else:
            return render(request,"product/update_category.html",{'form':form})
    return render(request,"product/update_category.html",{'form':Categoryform(instance=category)})  

def post_product(request):
      if request.method=="POST":
        form=Productform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_list")
        
        else:
            return render(request, "product/add_PRODUCT.html",{'form':form})
      return render(request,"product/add_product.html",{'form':Productform}) 

def update_product(request,product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        form = Productform(request.POST, request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
        else:
            return render(request, "product/update_product.html",{'form':form})
    return render(request,"product/update_product.html",{'form':Productform(instance=product)})




