from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
  queryset = Producto.objects.all()
  serializer_class = ProductoSerializer

  def get_queryset(self):
    negocio_id = self.request.query_params.get('negocio')
    if negocio_id:
      return self.queryset.filter(negocio_id=negocio_id)
    return self.queryset.none()
