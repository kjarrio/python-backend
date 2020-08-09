from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from estudantes import views

router = routers.DefaultRouter()
router.register(r'api/v1/estudante', views.EstudanteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
