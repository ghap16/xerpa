from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from common.validators import valid_image_extension


class Category(BaseModel):
    class CategoryType(models.TextChoices):
        EXPENSE = "EXPENSE", _("Expense")
        INCOME = "INCOME", _("Income")

    name = models.CharField(_("Name"), max_length=100, db_index=True)
    type = models.CharField(
        _("Type"),
        max_length=7,
        choices=CategoryType.choices,
        default=CategoryType.EXPENSE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        unique_together = [["name", "type"]]


class Merchant(BaseModel):
    merchant_name = models.CharField(_("Merchant name"), max_length=100, db_index=True)
    merchant_logo = models.URLField(
        _("Merchant logo"),
        max_length=256,
        blank=True,
        null=True,
        validators=[valid_image_extension],
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.merchant_name

    class Meta:
        verbose_name = _("Merchant")


class Keyword(BaseModel):
    keyword = models.CharField(_("Keyword"), max_length=25, db_index=True)
    merchant = models.ForeignKey(
        Merchant, on_delete=models.CASCADE, related_name="keywords"
    )

    def save(self, *args, **kwargs):
        self.keyword = self.keyword.lower()
        return super(Keyword, self).save(*args, **kwargs)

    def __str__(self):
        return self.keyword

    class Meta:
        verbose_name = _("Keyword")


class TransactionEnrichment(BaseModel):
    transaction = models.OneToOneField(
        "transactions.Transaction",
        on_delete=models.CASCADE,
        related_name="enrichment",
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Transaction ID: {self.transaction}"

    class Meta:
        verbose_name = _("Transaction Enrichment")
