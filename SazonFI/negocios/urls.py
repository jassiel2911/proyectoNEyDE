# negocios/urls.py
from django.urls import path
from . import views  # Importa tus vistas de la app 'negocios', incluida la nueva vista_html_productos_por_negocio

app_name = 'negocios' # Es una buena pr�ctica para organizar las URLs de las plantillas

urlpatterns = [
    # URL para la p�gina HTML que muestra los productos de un negocio espec�fico
    path('<int:id_negocio>/productos/', views.vista_html_productos_por_negocio, name='pagina_productos_de_negocio'),

    # Aqu� podr�as a�adir otras URLs que sirvan p�ginas HTML para la app 'negocios'.
    # Por ejemplo, si un due�o de negocio tiene un panel:
    # path('dashboard/', views.dashboard_negocio, name='dashboard_negocio'),
]