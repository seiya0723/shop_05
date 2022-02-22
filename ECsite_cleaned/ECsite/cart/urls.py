from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('edit/<uuid:pk>/', views.CartEdit, name='edit'),
    #path('delete/<uuid:pK>/', views.Delete, name='delete'),
    path('delete/<uuid:pk>/', views.Delete, name='delete'),
]
