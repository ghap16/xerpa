import json
import os
import random

from django.conf import settings
from django.utils.timezone import now
from rest_framework import status
from rest_framework.test import APITestCase

from transaction_enrichment.models import Category, Keyword, Merchant
from transactions.models import Transaction


class TransactionEnrichmentTests(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # TODO: I had to load the data this way since dumpdata didn't work
        # Load transacciones
        with open(
            os.path.join("fixtures", "transactions.json"), mode="r", encoding="utf-8"
        ) as json_data:
            data = json.load(json_data)
        bulk_transactions = []
        transacciones = [random.choice(data) for _ in range(1000)]
        for t in transacciones:
            bulk_transactions.append(
                Transaction(
                    description=t.get("description"), amount=t.get("amount"), date=now()
                )
            )
        transaction_objs = Transaction.objects.bulk_create(bulk_transactions)
        cls.transaction_ids = [str(t.id) for t in transaction_objs]

        # Load Categories
        with open(
            os.path.join("fixtures", "categories.json"), mode="r", encoding="utf-8"
        ) as json_data:
            data = json.load(json_data)
        bulk_categories = []
        for d in data:
            bulk_categories.append(
                Category(id=d.get("id"), name=d.get("name"), type=d.get("type"))
            )
        categories_objs = Category.objects.bulk_create(bulk_categories)
        cls.categories_ids = [str(d.id) for d in categories_objs]

        # Load merchant
        with open(
            os.path.join("fixtures", "merchants.json"), mode="r", encoding="utf-8"
        ) as json_data:
            data = json.load(json_data)
        bulk_merchants = []
        for d in data:
            bulk_merchants.append(
                Merchant(
                    id=d.get("id"),
                    merchant_name=d.get("name"),
                    merchant_logo=d.get("logo"),
                    category_id=d.get("category_id"),
                )
            )
        merchants_objs = Merchant.objects.bulk_create(bulk_merchants)
        cls.merchants_ids = [str(d.id) for d in merchants_objs]

        # Load Keywords
        with open(
            os.path.join("fixtures", "keywords.json"), mode="r", encoding="utf-8"
        ) as json_data:
            data = json.load(json_data)
        bulk_keywords = []
        for d in data:
            bulk_keywords.append(
                Keyword(
                    id=d.get("id"),
                    keyword=d.get("keyword"),
                    merchant_id=d.get("merchant_id"),
                )
            )
        keywords_objs = Keyword.objects.bulk_create(bulk_keywords)
        cls.keywords_ids = [str(d.id) for d in keywords_objs]

    def test_transaction_enrichment(self):
        """Assert that generate a pdf file sucessfully"""
        data = {"transactions": self.transaction_ids}
        response = self.client.post(
            "/api/v1/transactions/enrichment/", data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()

        self.assertEqual(len(self.transaction_ids), 1000)
        self.assertEqual(data["total_transactions_received"], len(self.transaction_ids))
        self.assertGreaterEqual(data["categorization_rate"], 0)
        self.assertGreaterEqual(data["identification_merchant_rate"], 0)
