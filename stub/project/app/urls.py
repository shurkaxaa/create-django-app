from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="CDN API",
      default_version='v1',
      description="API for CDN management",
      terms_of_service="https://<website.me>/cdn/policies/terms/",
      contact=openapi.Contact(email="<email@me>"),
      license=openapi.License(name="MIT"),
   ),
   validators=['flex', 'ssv'],
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
url(r'^api/v1/', include('api.urls')),
url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
