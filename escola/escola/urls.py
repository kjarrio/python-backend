from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers, permissions
from estudantes import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'api/v1/estudante', views.EstudanteViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="API de Estudantes",
      default_version='v1'
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
