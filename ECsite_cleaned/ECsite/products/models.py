from django.db import models
from django.utils import timezone

from django.conf import settings

import uuid


class ProductCategory(models.Model):
    # 本格的な運用を試みるのであれば、自動採番で予測されやすい数値型の主キーではなく、不規則な文字列が生成されるUUID型の主キーを使用するとセキュリティが向上する。
    # https://ja.wikipedia.org/wiki/UUID

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dt = models.DateTimeField(verbose_name="登録日時", default=timezone.now)
    name = models.CharField(verbose_name="カテゴリ名", max_length=20, unique=True,
                            error_messages={
                                    'unique': ("同一のカテゴリーが既に登録されています"),
                                },)

    def __str__(self):
        return self.name


class Product(models.Model):
    # 同じカテゴリと同じ商品名の組み合わせの登録は禁止にする。unique_togetherを使用する。
    # 例:名前の重複を禁止する場合、便箋用の『マスキングテープ』と工具用の『マスキングテープ』が同時に登録できないため、カテゴリと名前の組み合わせでの重複を禁止にする。
    # https://noauto-nolife.com/post/django-same-user-operate-prevent/

    class Meta:
        unique_together = ("category", "name")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dt = models.DateTimeField(verbose_name="登録日時", default=timezone.now)
    category = models.ForeignKey(ProductCategory, verbose_name="カテゴリ", on_delete=models.PROTECT)
    name = models.CharField(verbose_name="商品名", max_length=100, unique=True, error_messages={
                                    'unique': ("同一の商品が既に登録されています"),
                                },)
    description = models.CharField(verbose_name="商品説明", max_length=3000)
    price = models.PositiveIntegerField(verbose_name="価格")
    situation = models.BooleanField(verbose_name='販売状態')
    stock = models.PositiveIntegerField(verbose_name='在庫数')
    image = models.ImageField(verbose_name='サムネイル', null=True, blank=True, upload_to="shop/product_image/images/")

    # 1対多で関連づいた画像を全て取り出し、モデルオブジェクトのリストを返却。テンプレートではこれをループして1枚ずつ画像を出す。
    def images(self):
        return ProductImage.objects.filter(product=self.id).order_by("dt")

    def __str__(self):
        return self.name


# キャメルケースは↓のクラス名のように単語ごとに頭文字を大文字で連結する
class ProductImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dt = models.DateTimeField(verbose_name="登録日時", default=timezone.now)

    # スネークケースでアプリ名/モデルクラス名/フィールド名に保存する。
    # スネークケースは単語ごとに_を入れて全て小文字で連結する。
    image = models.ImageField(verbose_name="商品画像", upload_to="shop/product_image/images/")

    # 画像を指定する。1対多を使う。
    # 理由:商品に指定する画像の個数は、後からフレキシブルに変更できるようにする必要がある。そのため、ProductにImageFieldを複数追加する方法は望ましくない。
    product = models.ForeignKey(Product, verbose_name="対象商品", on_delete=models.CASCADE)