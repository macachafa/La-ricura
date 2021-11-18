from rest_framework import serializers
from authApp.models.producto import Producto
from authApp.models.categoria import Categoria
from authApp.models.proveedor import Proveedor
from authApp.serializers.proveedorSerializer import SupplierSerializer
from authApp.serializers.categoriaSerializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
  
  

  class Meta:
    model = Producto
    fields = ['nombre', 'unidadMedida', 'stock', 'idCategoria','idProveedor'] #Campos a pasar por el usuario

  '''def create(self, validated_data):
        producto = Producto.objects.create(**validated_data)
        categoria_data = validated_data.pop('idCategoria') 
        proveedor_data = validated_data.pop('idProveedor')
        return producto'''

  def create(self, data):
        
        productoInstance = Producto.objects.create(**data)
       
        return productoInstance

  def to_representation(self, obj):
    producto = Producto.objects.get(id=obj.id)
    categoria = Categoria.objects.get(idCategoria=obj.id)
    proveedor = Proveedor.objects.get(idProveedor=obj.id)
    
    return {
      'id': producto.id,        #Información a mostrar al usuario
      'nombre': producto.nombre,
      'unidadMedida': producto.unidadMedida, 
      'stock': producto.stock,
      'categoria': categoria.categoria,
      'proveedor': proveedor.nombre,
      'idCategoria': categoria.id,
      'idProveedor': proveedor.id
        
        
    }
