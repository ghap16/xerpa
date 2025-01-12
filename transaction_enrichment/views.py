from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, Keyword, Merchant
from .processing_enrichment import proccessing_enrichment
from .serializers import (
    CategorySerializer,
    KeywordSerializer,
    MerchantSerializer,
    TransactionEnrichmentRequestSerializer,
    TransactionEnrichmentResponseSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer


class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


@swagger_auto_schema(
    methods=["post"], request_body=TransactionEnrichmentRequestSerializer
)
@api_view(["POST"])
def proccessing_enrichment_view(request):
    serializer = TransactionEnrichmentRequestSerializer(data=request.data)
    if serializer.is_valid():
        total = len(serializer.data["transactions"])
        categorization_count, identification_merchant_count = proccessing_enrichment(
            serializer.data
        )
        serializer = TransactionEnrichmentResponseSerializer(
            data={
                "total_transactions_received": total,
                "categorization_rate": categorization_count * 100 / total,
                "identification_merchant_rate": identification_merchant_count
                * 100
                / total,
            }
        )
        return Response(serializer.initial_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
