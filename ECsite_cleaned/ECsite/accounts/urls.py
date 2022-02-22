from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('my_page/<uuid:pk>/', views.MyPage, name='my_page'),
    path('accounts_edit/<uuid:pk>/', views.AccountsEdit, name='accounts_edit'),
]