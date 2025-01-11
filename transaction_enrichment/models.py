from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel
from common.validators import valid_image_extension


class Category(BaseModel):
    class CategoryType(models.TextChoices):
        EXPENSE = "EXPENSE", _("Expense")
        INCOME = "INCOME", _("Income")

    name = models.CharField(_("Name"), max_length=100)
    type = models.CharField(_('Type'), max_length=7, choices=CategoryType, default=CategoryType.EXPENSE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Merchant(BaseModel):
    merchant_name = models.CharField(_('Merchant name'), max_length=100)
    merchant_logo = models.URLField(_('Merchant logo'), max_length=256, null=True, validators=[valid_image_extension])
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.merchant_name
    
    class Meta:
        verbose_name = _('Merchant')


class Keyword(BaseModel):
    keyword = models.CharField(_('Keyword'), max_length=100)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)

    def __str__(self):
        return self.keyword
    
    class Meta:
        verbose_name = _('Keyword')


class TransactionEnrichment(BaseModel):
    transaction = models.OneToOneField('transactions.Transaction', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Transaction ID: {self.transaction}"
    
    class Meta:
        verbose_name = _('Transaction Enrichment')