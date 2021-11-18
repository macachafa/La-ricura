from rest_framework import serializers
from authApp.models.proveedor import Proveedor

class SupplierSerializer(serializers.ModelSerializer):
  class Meta:
    model = Proveedor
    fields = ['id','nombre', 'tel', 'ciudad', 'correo'] 