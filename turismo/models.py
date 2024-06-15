from django.db import models

# Create your models here.
class Servicios(models.Model):
        id_servicio = models.AutoField(db_column='idServicio', primary_key=True)
        precio = models.CharField(max_length=10, null=True, default=None)
        imagen = models.ImageField(upload_to='servicios', null=True)
        descripcion = models.CharField(max_length=100)
        def __str__(self):
            return str(self.id_servicio)
