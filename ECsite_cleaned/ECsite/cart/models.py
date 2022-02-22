from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator
from products.models import Product

import uuid

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dt = models.DateTimeField(verbose_name="カート追加日時", default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="カート所有者", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="商品", on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name="商品の個数", default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.product.name

    def get_total_price(self):
        return self.product.price * self.amount
