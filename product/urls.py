from django.urls import path
from .import views

urlpatterns=[
    path('products/',views.get_all_product,name="product_list"),

]