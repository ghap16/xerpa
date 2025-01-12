from rest_framework.routers import DefaultRouter

from transaction_enrichment.views import (
    CategoryViewSet,
    KeywordViewSet,
    MerchantViewSet,
)
from transactions.views import TransactionViewSet

router = DefaultRouter()
router.register(r"transactions", TransactionViewSet, basename="transaction")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"merchants", MerchantViewSet, basename="merchant")
router.register(r"keywords", KeywordViewSet, basename="keyword")
