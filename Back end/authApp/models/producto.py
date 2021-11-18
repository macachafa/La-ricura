from django.db import models
from django.db.models.deletion import CASCADE 
# from .user import User
from .categoria import Categoria
from .proveedor import Proveedor

class Producto(models.Model):  
  id = models.AutoField(primary_key=True)
  nombre = models.CharField('nombre', max_length = 50)
  unidadMedida = models.CharField('unidadMedida', max_length = 50)
  stock = models.IntegerField('stock', max_length = 50)
  idCategoria = models.ForeignKey(Categoria, related_name='idCategoria' ,on_delete= models.CASCADE)  #on_delete=models.SET_NULL, null=True
  # related_name es lo que me devuelve la llave foránea
  idProveedor = models.ForeignKey(Proveedor, related_name="idProveedor",on_delete= models.CASCADE)