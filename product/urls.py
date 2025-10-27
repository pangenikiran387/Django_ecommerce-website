from django.urls import path
from . import views

urlpatterns = [

    path('products/', views.get_all_product, name="product_list"),
    path('add-product/',views.post_product,name="add_product"),
    path('update-product/<product_id>/', views.update_product , name="update_product"),
    path('products/<int:product_id>/', views.delete_product, name="delete_product"),
    path('categories/<int:category_id>/', views.delete_category, name="delete_category"),
    path('categories/', views.category_list, name="category_list"),
    path('add-category/', views.add_category, name="add_category"),
    path('update-category/<int:category_id>/', views.update_category , name="update_category"),
]
