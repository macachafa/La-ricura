from django.db import models 


class Proveedor(models.Model):
  id = models.AutoField(primary_key=True)
  nombre = models.CharField('nombre', max_length = 100, unique=True)
  tel = models.CharField('tel', max_length= 30)
  ciudad = models.CharField('ciudad', max_length= 40)
  correo = models.EmailField('correo', max_length= 40)