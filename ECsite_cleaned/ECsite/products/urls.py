from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('products_category/', views.ProductsCategory, name='products_category'),
    path('products/', views.Products, name='products'),
    path('products_images', views.ProductsImages, name='products_images'),
    path('product_detail/<uuid:pk>/', views.ProductsDetail, name='product_detail'),
    path('edit/<uuid:pk>/', views.Edit, name='edit'),
]