import re

from django.core.cache import cache
from django.db.models import Prefetch

from transaction_enrichment.models import Category, Merchant, TransactionEnrichment
from transactions.models import Transaction


def description_list(description: str, min=2):
    description_list = re.sub("[^\w]", " ", description.lower()).split()
    return list(filter(lambda word: len(word) > min, description_list))


def proccessing_enrichment(data) -> tuple:
    categorization_count = 0
    identification_merchant_count = 0

    data_clean = list(set(data["transactions"]))
    transactions = Transaction.objects.filter(pk__in=data_clean)

    for transaction in transactions:
        if transaction_find_keyword_or_merchant(transaction):
            categorization_count += 1
            identification_merchant_count += 1
            continue

        if transaction_find_category(transaction):
            identification_merchant_count += 1

    return categorization_count, identification_merchant_count


def transaction_find_keyword_or_merchant(transaction: Transaction) -> bool:
    founded = False
    description_l = description_list(transaction.description)

    for merchant in get_merchant():
        if not category_type_is_correct(transaction.amount, merchant["category_type"]):
            continue

        if len(merchant["keywords"]) > 0 and any(
            word in description_l for word in merchant["keywords"]
        ):
            save_enrichment(transaction, merchant)
            founded = True
            break

        name_list = re.sub("[^\w]", " ", merchant["name"].lower()).split()
        name_list = list(filter(lambda word: len(word) > 2, name_list))
        if all(word in description_l for word in name_list):
            save_enrichment(transaction, merchant)
            founded = True
            break

    return founded


def transaction_find_category(transaction: Transaction) -> bool:
    founded = False
    description_l = description_list(transaction.description, min=3)

    for category in get_category():
        if not category_type_is_correct(transaction.amount, category["type"]):
            continue

        name_list = re.sub("[^\w]", " ", category["name"].lower()).split()
        name_list = list(filter(lambda word: len(word) > 3, name_list))
        if all(word in description_l for word in name_list):
            save_enrichment(transaction, {"category_id": category["id"]})
            founded = True
            break

    return founded


def get_category() -> list:
    category_cache = cache.get("category")
    if not category_cache:
        categorys = Category.objects.only("id", "name", "type")
        category_cache = [
            {
                "id": m.id,
                "name": m.name,
                "type": m.type,
            }
            for m in categorys
        ]
        cache.set("category", category_cache, timeout=3000)
    return category_cache


def get_merchant() -> list:
    merchant_cache = cache.get("merchant")
    if not merchant_cache:
        merchants = Merchant.objects.prefetch_related(
            Prefetch("keywords", to_attr="keywords_list"),
        ).select_related("category")
        merchant_cache = [
            {
                "merchant_id": m.id,
                "name": m.merchant_name,
                "keywords": [kw.keyword for kw in m.keywords_list],
                "category_id": m.category_id,
                "category_type": m.category.type,
            }
            for m in merchants
        ]
        cache.set("merchant", merchant_cache, timeout=3000)
    return merchant_cache


def category_type_is_correct(amount, category_type) -> bool:
    if amount > 0 and category_type == Category.CategoryType.INCOME:
        return True
    if amount < 0 and category_type == Category.CategoryType.EXPENSE:
        return True
    return False


def save_enrichment(transaction: Transaction, data: dict):
    TransactionEnrichment.objects.update_or_create(
        transaction_id=transaction.id,
        defaults={
            "category_id": data.get("category_id", None),
            "merchant_id": data.get("merchant_id", None),
        },
    )
