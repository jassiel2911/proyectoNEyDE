from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from .models import Negocio
from productos.models import Producto
from .serializers import NegocioSerializer
from productos.serializers import ProductoSerializer

User = get_user_model()

class NegocioViewSet(viewsets.ModelViewSet):
    serializer_class = NegocioSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Negocio.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        try:
            instance = self.get_object()
            if instance.usuario == self.request.user:
                serializer.save()
            else:
                return Response(
                    {"error": "No tienes permiso para actualizar este negocio."},
                    status=status.HTTP_403_FORBIDDEN,
                )
        except Negocio.DoesNotExist:
            return Response(
                {"error": "Negocio no encontrado."}, status=status.HTTP_404_NOT_FOUND
            )

    def perform_destroy(self, instance):
        if instance.usuario == self.request.user:
            instance.delete()
        else:
            return Response(
                {"error": "No tienes permiso para eliminar este negocio."},
                status=status.HTTP_403_FORBIDDEN,
            )

    @action(detail=True, methods=['get'])
    def productos(self, request, pk=None):
        try:
            negocio = self.get_object()
            if negocio.usuario == self.request.user:
                productos = negocio.producto_set.all()
                return Response(
                    {"productos": [{"id": p.id, "nombre": p.nombre} for p in productos]},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "No tienes permiso para ver los productos de este negocio."},
                    status=status.HTTP_403_FORBIDDEN,
                )
        except Negocio.DoesNotExist:
            return Response(
                {"error": "Negocio no encontrado."}, status=status.HTTP_404_NOT_FOUND
            )


class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        negocio_id = self.kwargs.get('negocio_pk')
        return Producto.objects.filter(negocio__id=negocio_id, negocio__usuario=self.request.user)

    def perform_create(self, serializer):
        negocio_id = self.kwargs.get('negocio_pk')
        negocio = Negocio.objects.get(id=negocio_id, usuario=self.request.user)
        serializer.save(negocio=negocio)

    def perform_update(self, serializer):
        try:
            producto = self.get_object()  # Esto obtiene el producto basado en el id
            # Asegúrate de que el producto pertenece al negocio y usuario correctos
            if producto.negocio.usuario == self.request.user:
                serializer.save()
            else:
                return Response(
                    {"error": "No tienes permiso para actualizar este producto."},
                    status=status.HTTP_403_FORBIDDEN,
                )
        except Producto.DoesNotExist:
            raise NotFound({"error": "Producto no encontrado."})  # Esto maneja correctamente el caso cuando no se encuentra el producto

    def perform_destroy(self, instance):
        if instance.negocio.usuario == self.request.user:
            instance.delete()
        else:
            return Response(
                {"error": "No tienes permiso para eliminar este producto."},
                status=status.HTTP_403_FORBIDDEN,
            )