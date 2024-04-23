from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from home import settings
from django.conf.urls import url
from django.urls import include, path
from django.conf.urls import url
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
# -*- coding: utf-8 -*-

from django.urls import path ,include
from django.conf.urls.i18n import i18n_patterns
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [

                  path('admin/', admin.site.urls),
                  path('i18n/', include('django.conf.urls.i18n')),
                  path("", include("api.url")),
                  path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
