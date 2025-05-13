from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from .views import RegistroUsuarioViewSet, InicioSesionAPIView
from negocios.views import NegocioViewSet
from productos.views import ProductoViewSet

# Router principal
router = routers.DefaultRouter()
router.register(r'registro', RegistroUsuarioViewSet, basename='registro')
router.register(r'negocios', NegocioViewSet, basename='negocios')
router.register(r'productos', ProductoViewSet, basename='productos')  # -> /productos/ y /productos/{id}/
router.register(r'negocios/(?P<negocio_pk>\d+)/productos', ProductoViewSet)  # -> /negocios/{negocio_pk}/productos/

# Router anidado para productos dentro de negocios
negocio_router = nested_routers.NestedDefaultRouter(router, r'negocios', lookup='negocio')
negocio_router.register(r'productos', ProductoViewSet, basename='negocio-productos')  # -> /negocios/{negocio_pk}/productos/

urlpatterns = [
    path('', include(router.urls)),
    path('', include(negocio_router.urls)),
    path('login/', InicioSesionAPIView.as_view(), name='api-login'),
    path('api/', include(router.urls)),
    path('', include(negocio_router.urls)),
]