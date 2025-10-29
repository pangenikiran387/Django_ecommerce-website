from django.urls import path
from . import views
urlpatterns=[
    path('',views.home_page,name="home-page"),
    path('product/<int:pk>/',views.product_detail, name="product-detail")
]