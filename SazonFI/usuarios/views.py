from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]  #  Para permitir el registro de nuevos usuarios

