from django.urls import include, path

from transaction_enrichment.views import proccessing_enrichment_view

from .routers import router
from .swagger import schema_view

urlpatterns = [
    path("v1/transactions/enrichment/", proccessing_enrichment_view, name="enrichment"),
    path("v1/", include(router.get_urls())),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="swagger",
    ),
]
