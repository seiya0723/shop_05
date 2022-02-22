from django.shortcuts import render, redirect
from django.views.generic import View

from accounts.models import CustomUser
from .models import Contacts
from .forms import ContactForm

class ContactView(View):
    def get(self, request, *args, **kwargs):

        user = CustomUser.objects.all()
        content = Contacts.objects.all()

        context = {'contents': content,
                   'users': user}

        return render(request, 'contacts/contact.html', context)

    def post(self, request, *args, **kwargs):

        copied = request.POST.copy()
        copied['user_id'] = request.user.id

        form = ContactForm(copied)

        if form.is_valid():
            print('バリデーションOK')
            form.save()
        else:
            print('バリデーションNG')
            print(form.errors)

        return redirect('contacts:contact')

contact = ContactView.as_view()