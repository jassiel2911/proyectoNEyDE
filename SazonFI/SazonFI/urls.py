from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # URLs de la API (usuarios, negocios)
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', TemplateView.as_view(template_name='usuarios/login.html'), name='login'),
    path('registro/', TemplateView.as_view(template_name='usuarios/registro.html'), name='registro'),
    path('negocio/', TemplateView.as_view(template_name='negocio/negocio.html'), name='negocio'),
    path('cliente/', TemplateView.as_view(template_name='cliente/cliente.html'), name='cliente'),
]