# Generated by Django 4.0.6 on 2022-07-12 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=20, verbose_name='Categoria  ')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('stock', models.IntegerField(verbose_name='Precio')),
            ],
        ),
    ]
