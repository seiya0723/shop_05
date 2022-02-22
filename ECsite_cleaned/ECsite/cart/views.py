from django.shortcuts import render, redirect
from django.views.generic import View

from accounts.models import CustomUser
from products.models import Product

from .models import Cart
from .forms import CartForm, CartEditForm

# class CartView(View):
#
#     def get(self, request, *args, **kwargs):
#         #ここでカートの中身を表示
#
#         context = {}
#
#         if request.user.is_authenticated:
#             context["carts"] = Cart.objects.filter(user=request.user.id)
#         else:
#             pass
#
#         return render(request, "accounts/cart.html", context)
#
# cart = CartView.as_view()

class CartView(View):

    def get(self, request, *args, **kwargs):
        #ここでカートの中身を表示

        context = {}

        if request.user.is_authenticated:

            carts = Cart.objects.filter(user=request.user.id)
            context["num"] = Cart.objects.filter(user=request.user.id).count()

            context["total"] = 0
            for cart in carts:
                context["total"] += cart.get_total_price()

            context["carts"] = carts

        else:
            #TODO:未認証ユーザーにはCookie格納されたカートのデータを表示するのも良い
            pass
        return render(request, "cart/cart.html", context)

cart = CartView.as_view()

class CartEditView(View):
    def get(self, request, pk, *args, **kwargs):

        context = {}

        context['products'] = Cart.objects.filter(product=pk).first()

        # product = Cart.objects.filter(product=pk).first()
        # context = {"products": product}

        return render(request, "cart/cart.html", context)

    def post(self, request, pk, *args, **kwargs):

        product = Cart.objects.filter(user=request.user.id, product=pk).first()

        copied = request.POST.copy()
        copied["user"] = request.user.id
        copied["product"] = pk

        form = CartForm(copied, instance=product)

        if not form.is_valid():
            print("バリデーションNG")
            print(form.errors)
            return redirect("cart:cart")

        cart = Cart.objects.filter(user=request.user.id, product=pk).first()

        if cart:
            cleaned = form.clean()
    
            #TODO:数量0であれば削除する
            if cleaned["amount"] == 0:
                cart.delete()
                return redirect("cart:cart")


            stock = Product.objects.filter(id=pk).first().stock

            #TODO:ここで数量を編集するときも加算として扱われる
            if stock >= cart.amount + cleaned["amount"]:
                cart.amount += cleaned["amount"]
                cart.save()

            else:
                print("在庫数を超過しているため、カートに追加できません。")

        else:
            # 存在しない場合は新規作成
            form.save()

        # if form.is_valid():
        #     print("バリデーションOK")
        #     form.save()
        # else:
        #     print("バリデーションNG")
        #     print(form.errors)

        return redirect("cart:cart")

CartEdit = CartEditView.as_view()

class DeleteView(View):
    def post(self, request, pk, *args, **kwargs):

        """
        product = Cart.objects.filter(product=pk).first()

        if product:
            print("削除")
            product.delete()
        else:
            print("対象のデータは見つかりませんでした。")
        """

        #ここでユーザーidも含めて検索する。
        cart = Cart.objects.filter(id=pk,user=request.user.id).first()

        if cart:
            print("削除")
            cart.delete()
        else:
            print("対象のデータは見つかりませんでした。")


        return redirect("cart:cart")

Delete = DeleteView.as_view()
