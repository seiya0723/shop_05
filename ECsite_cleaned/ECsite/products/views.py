from django.shortcuts import render, redirect
from django.views.generic import View

from .models import ProductCategory, Product, ProductImage
from .forms import ProductCategoryForm, ProductForm, ProductsImageForm, EditForm

from cart.models import Cart
from cart.forms import CartForm

class ProductsView(View):
    def get(self, request, *args, **kwargs):

        context = {}

        context['products'] = Product.objects.all()
        context['categories'] =ProductCategory.objects.all()
        context['images'] = ProductImage.objects.all()

        # product = Product.objects.all()
        # category = ProductCategory.objects.all()
        # image = ProductImage.objects.all()
        #
        # context = {'products': product,
        #            'categories': category,
        #            'images': image}

        return render(request, 'products/products_create.html', context)

    def post(self, request, *args, **kwargs):

        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            print('バリデーションOK')
            form.save()
        else:
            print('バリデーションNG')
            print(form.errors)

        return redirect('products:products')

Products = ProductsView.as_view()

class ProductCategoryView(View):
    def post(self, request, *args, **kwargs):

        form = ProductCategoryForm(request.POST)

        if form.is_valid():
            print('バリデーションOK')
            form.save()
        else:
            print('バリデーションNG')
            print(form.errors)

        return redirect('products:products')

ProductsCategory = ProductCategoryView.as_view()

class ProductImagesView(View):
    def post(self, request, *args, **kwargs):

        form = ProductsImageForm(request.POST)

        if form.is_valid():
            print('バリデーションOK')
            form.save()
        else:
            print('バリデーションNG')
            print(form.errors)

        return redirect('products:products')

ProductsImages = ProductImagesView.as_view()

class ProductDetailView(View):
    def get(self, request, pk, *args, **kwargs):

        context = {}

        context['products'] = Product.objects.filter(id=pk).first()
        context['images'] = ProductImage.objects.filter(product_id=pk)
        context["num"] = Cart.objects.filter(user=request.user.id).count()

        # product = Product.objects.filter(id=pk).first()
        # image = ProductImage.objects.filter(product_id=pk)
        #
        # context = {'products': product,
        #            'images': image}

        return render(request, 'products/product_detail.html', context)

    # def post(self, request, pk, *args, **kwargs):
    #
    #     if request.user.is_authenticated:
    #         # TIPS:ここで既に同じ商品がカートに入っている場合、レコード新規作成ではなく、既存レコードにamount分だけ追加する。
    #
    #         copied = request.POST.copy()
    #
    #         copied["user"] = request.user.id
    #         copied["product"] = pk
    #
    #         form = CartForm(copied)
    #
    #         if form.is_valid():
    #             print("バリデーションOK")
    #
    #         cart = Cart.objects.filter(user=request.user.id, product=pk).first()
    #
    #         if cart:
    #             cleaned = form.clean()
    #             cart.amount += cleaned["amount"]
    #             cart.save()
    #         else:
    #             form.save()
    #             redirect('products:product_detail', pk)
    #     else:
    #             print("未認証です")
    #             return redirect('account_login')

    def post(self, request, pk, *args, **kwargs):

        # ここでユーザーのカートへ追加
        if request.user.is_authenticated:
            # TIPS:ここで既に同じ商品がカートに入っている場合、レコード新規作成ではなく、既存レコードにamount分だけ追加する。
            copied = request.POST.copy()

            copied["user"] = request.user.id
            copied["product"] = pk

            form = CartForm(copied)

            if not form.is_valid():
                print("バリデーションNG")
                return redirect("products:product_detail", pk)

            # print("バリデーションOK")

            # TIPS:ここで既に同じ商品がカートに入っている場合、レコード新規作成ではなく、既存レコードにamount分だけ追加する。
            cart = Cart.objects.filter(user=request.user.id, product=pk).first()

            if cart:
                cleaned = form.clean()

                # TODO:ここでカートに数量を追加する時、追加される数量が在庫数を上回っていないかチェックする。上回る場合は拒否する。
                stock = Product.objects.filter(id=pk).first().stock

                if stock >= cart.amount + cleaned["amount"]:
                    # カート内商品は在庫数以下につき、保存OK
                    cart.amount += cleaned["amount"]
                    cart.save()

                else:
                    print("在庫数を超過しているため、カートに追加できません。")

            else:
                # 存在しない場合は新規作成
                form.save()

        else:
            print("未認証です")
            return redirect('account_login')
            # TODO:未認証ユーザーにはCookieにカートのデータを格納するのも良い

        return redirect("products:product_detail", pk)

ProductsDetail = ProductDetailView.as_view()

class ProductEditView(View):
    def get(self, request, pk, *args, **kwargs):

        context = {}

        context['products'] = Product.objects.filter(id=pk).first()
        context['categories'] = ProductCategory.objects.all()

        # product = Product.objects.filter(id=pk).first()
        # category = ProductCategory.objects.all()
        # context = {'products': product,
        #            'categories': category}

        return render(request, 'products/edit.html', context)

    def post(self, request, pk, *args, **kwargs):

        product = Product.objects.filter(id=pk).first()

        form = EditForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            print('バリデーションOK')
            form.save()
        else:
            print('バリデーションNG')
            print(form.errors)

        return redirect('products:edit', pk)

Edit = ProductEditView.as_view()