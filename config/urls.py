from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


schema_view = get_schema_view(
    openapi.Info(
        title="Fundación Altius",
        default_version="v1",
        description="Mercado Fundación Altius",
        contact=openapi.Contact(email="tecnicoinformatico@fundacionaltius.org"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(SessionAuthentication, JWTAuthentication),
    #    security=[{"Bearer": []}],  # This adds Bearer token to Swagger UI
)

urlpatterns = [
    path("auth/", include("custom_auth.urls")),
    path("inventory/", include("inventory.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
urlpatterns += i18n_patterns(
    path(_("admin/"), admin.site.urls),
)
