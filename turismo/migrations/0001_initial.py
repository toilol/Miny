# Generated by Django 5.0.6 on 2024-06-14 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id_servicio', models.AutoField(db_column='idServicio', primary_key=True, serialize=False)),
                ('precio', models.CharField(default=None, max_length=10, null=True)),
                ('imagen', models.ImageField(default=None, null=True, upload_to='templates/turismo/fotos')),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]
