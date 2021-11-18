from rest_framework import serializers
from authApp.models.categoria import Categoria

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Categoria
    fields = ['id','categoria'] # Solo quero mostrar el nombre (sin el id)