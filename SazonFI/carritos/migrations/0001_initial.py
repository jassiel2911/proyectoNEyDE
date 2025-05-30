# Generated by Django 5.2 on 2025-05-14 17:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('negocios', '0002_negocio_id_alter_negocio_usuario'),
        ('productos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('actualizado_en', models.DateTimeField(auto_now=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='carrito', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('precio_al_agregar', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('agregado_en', models.DateTimeField(auto_now_add=True)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='carritos.carrito')),
                ('negocio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='negocios.negocio')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
        ),
    ]
