from django.db import models

from django.conf import settings

import uuid

class Contacts(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='ユーザーID')
    name = models.CharField(verbose_name='名前', max_length=10)
    email = models.EmailField(verbose_name='メールアドレス', max_length=200)
    title = models.CharField(verbose_name='タイトル', max_length=100)
    contents = models.CharField(verbose_name='お問い合わせ内容', max_length=3000)

    def __str__(self):
        return self.title