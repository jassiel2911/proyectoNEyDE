from django.db import models
from usuarios.models import Usuario

class Negocio(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Cambiado a ForeignKey
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, blank=True)
    horario_apertura = models.TimeField(null=True, blank=True)
    horario_cierre = models.TimeField(null=True, blank=True)
    logo = models.ImageField(upload_to='negocios/logos/', null=True, blank=True)

    def __str__(self):
        return self.nombre