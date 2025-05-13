from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NegocioViewSet

router = DefaultRouter()
router.register(r'', NegocioViewSet, basename='negocios')

urlpatterns = [
  path('', include(router.urls)),
]
