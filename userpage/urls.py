from django.urls import path
from . import views
urlpatterns=[
    path('',views.home_page,name="home-page"),
    path('cart/',views.show_cart_items,name="all-cart-items"),
    path('product/<int:pk>/',views.product_detail, name="product-detail"),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name="add_to_cart"),
   

    # path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),

]