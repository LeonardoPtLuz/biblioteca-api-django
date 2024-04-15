
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from livros_app.api import viewsets as livrosviewsets
from django.conf.urls.static import static
from django.conf import settings

route = routers.DefaultRouter()

route.register(r'livros', livrosviewsets.LivrosViewSet, basename="Livros")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
