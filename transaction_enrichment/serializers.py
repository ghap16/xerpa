from rest_framework import serializers

from .models import Category, Keyword, Merchant


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "type", "created_at", "updated_at"]


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = [
            "id",
            "merchant_name",
            "merchant_logo",
            "category",
            "created_at",
            "updated_at",
        ]


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ["id", "keyword", "merchant", "created_at", "updated_at"]


class TransactionEnrichmentRequestSerializer(serializers.Serializer):
    transactions = serializers.ListField(child=serializers.UUIDField())


class TransactionEnrichmentResponseSerializer(serializers.Serializer):
    total_transactions_received = serializers.IntegerField(max_value=10000)
    categorization_rate = serializers.DecimalField(max_digits=5, decimal_places=2)
    identification_merchant_rate = serializers.DecimalField(
        max_digits=5, decimal_places=2
    )
