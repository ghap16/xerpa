from django.contrib import admin

from .models import Category, Keyword, Merchant, TransactionEnrichment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    pass


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    pass


@admin.register(TransactionEnrichment)
class TransactionEnrichmentAdmin(admin.ModelAdmin):
    pass
