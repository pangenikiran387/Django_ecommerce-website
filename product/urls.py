from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.get_all_product, name="product_list"),
    path('products/<int:product_id>/', views.delete_product, name="delete_product"),
    path('categories/<int:category_id>/', views.delete_category, name="delete_category"),
    path('categories/', views.category_list, name="category_list"),
]
