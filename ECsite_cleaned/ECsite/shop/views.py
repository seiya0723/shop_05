from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import CustomUser

from products.models import Product, ProductCategory, ProductImage

from cart.models import Cart

class HomeView(View):
    def get(self, request, *args, **kwargs):

        context = {}

        context['products'] = Product.objects.all()
        context['categories'] = ProductCategory.objects.all()
        context['images'] = ProductImage.objects.all()
        context['users'] = CustomUser.objects.all()
        context["num"] = Cart.objects.filter(user=request.user.id).count()

        # product = Product.objects.all()
        # category = ProductCategory.objects.all()
        # image = ProductImage.objects.all()
        # user = CustomUser.objects.all()
        #
        # context = {'products': product,
        #            'categories': category,
        #            'images': image,
        #            'users': user}

        return render(request, 'shop/home.html', context)

Home = HomeView.as_view()

