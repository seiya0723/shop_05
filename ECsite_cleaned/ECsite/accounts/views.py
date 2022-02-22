from django.shortcuts import render, redirect
from django.views.generic import View

from .models import CustomUser

from .forms import SignupForm, AccountEditForm

class AccountsMyPage(View):
    def get(self, request, pk, *args, **kwargs):

        context = {}

        context['object'] = CustomUser.objects.filter(id=pk).first()

        return render(request, 'accounts/accounts_my_page.html', context)

MyPage = AccountsMyPage.as_view()

class AccountsEditView(View):

    def get(self, request, pk, *args, **kwargs):

        account = CustomUser.objects.filter(id=pk).first()
        context = {"accounts": account}

        return render(request, "accounts/accounts_edit.html", context)

    def post(self, request, pk, *args, **kwargs):

        account = CustomUser.objects.filter(id=pk).first()

        form = AccountEditForm(request.POST, request.FILES, instance=account)

        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print("バリデーションNG")
            print(form.errors)

        return redirect("accounts:accounts_edit", pk)

AccountsEdit = AccountsEditView.as_view()