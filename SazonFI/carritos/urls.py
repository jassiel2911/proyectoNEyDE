# carritos/urls.py
from django.urls import path
from . import views

app_name = 'carritos' # Buena pr�ctica

urlpatterns = [
    path('', views.vista_carrito, name='ver_carrito'), # URL para ver el carrito (ej: /carrito/)
    # Aqu� tambi�n podr�an ir las URLs de API para el carrito si decides no ponerlas en api/urls.py
    # Pero por ahora, mantendremos la API /api/carrito/agregar/ en api/urls.py
]