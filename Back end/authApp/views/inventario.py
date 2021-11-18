'''from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authApp.serializers.productoSerializer import ProductSerializer'''

# Código profe Brayan

from django.db.models import query
from django.views import generic
from rest_framework import views, status
from rest_framework.response import Response # clase para respuestas
from rest_framework import generics
# model
from authApp.models import Producto, producto
from authApp.models.categoria import Categoria
from authApp.models.proveedor import Proveedor
#serializer
from authApp.serializers import ProductSerializer, SupplierSerializer, productoserilizer
from authApp.serializers.categoriaSerializer import CategorySerializer

#Prueba
class TestViews(views.APIView):
    def get(self, request):
        response = {"message": "Esto es una prueba"}
        return Response(data=response, status=status.HTTP_200_OK)

#Producto
class ProductView(views.APIView):
    def get(self, request):
        queryset = Producto.objects.all() # listado de objetos
        serializer = ProductSerializer(data=queryset, many=True)
        serializer.is_valid()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
class ProductActualizar(views.APIView):
    def get(self, request, pk):
        queryset = Producto.objects.filter(id=pk)
        serializer = ProductSerializer(data=queryset, many=True)
        serializer.is_valid()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
         queryset = Producto.objects.filter(id=pk)
         queryset.delete()
         return Response("eliminado")
 
    def put(self, request, pk):
        queryset = Producto.objects.get(id=pk)
        serializer = ProductSerializer(queryset,data=request.data) # convierte el JSON en un objeto
        if serializer.is_valid():
            serializer.save() #se actualizo en la base de datos
            data = {"message": "Se actualizo"}
            return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductCreate(views.APIView):
    def post(self, request):
        print("Información obtenida", request.data) # es el JSON que ingresa el usuario
        serializer = ProductSerializer(data=request.data) # convierte el JSON en un objeto
        if serializer.is_valid():
            serializer.save() #Quedó guardado en la base de datos
            data = {"message": "Se creó exiosamente el producto"}
            return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


        


#Proveedor
class SupplierCreate(views.APIView):
    def post(self, request):
        print("Información obtenida", request.data) # es el JSON que ingresa el usuario
        serializer = SupplierSerializer(data=request.data) # convierte el JSON en un objeto
        if serializer.is_valid():
            serializer.save() #Quedó guardado en la base de datos
            data = {"message": "Se creó exiosamente el proveedor"}
            return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SupplierActualizar(views.APIView):
    def get(self, request, pk):
        queryset = Proveedor.objects.filter(id=pk)
        serializer = SupplierSerializer(data=queryset, many=True)
        serializer.is_valid()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
         queryset = Proveedor.objects.filter(id=pk)
         queryset.delete()
         return Response("eliminado")
 
    def put(self, request, pk):
        queryset = Proveedor.objects.get(id=pk)
        serializer = SupplierSerializer(queryset,data=request.data) # convierte el JSON en un objeto
        if serializer.is_valid():
            serializer.save() #Quedó guardado en la base de datos
            data = {"message": "Se actualizo el proveedor"}
            return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SupplierView(views.APIView):
    def get(self, request):
        queryset = Proveedor.objects.all() # listado de objetos
        serializer = SupplierSerializer(data=queryset, many=True)
        serializer.is_valid()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

#Categoría
class CategoryCreate(views.APIView):
    def post(self, request):
        print("Información obtenida", request.data) # es el JSON que ingresa el usuario
        serializer = CategorySerializer(data=request.data) # convierte el JSON en un objeto
        if serializer.is_valid():
            serializer.save() #Quedó guardado en la base de datos
            data = {"message": "Se creó exiosamente la categoría"}
            return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CategoryActualizar(views.APIView):
    def get(self, request, pk):
        queryset =Categoria.objects.filter(id=pk)
        serializer = CategorySerializer(data=queryset, many=True)
        serializer.is_valid()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
         queryset= Categoria.objects.filter(id=pk)
         queryset.delete()
         return Response("eliminado")
 
    def put(self, request, pk):
        queryset = Categoria.objects.get(id=pk)
        serializer = CategorySerializer(queryset,data=request.data) # convierte el JSON en un objeto
        if serializer.is_valid():
            serializer.save() #Quedó guardado en la base de datos
            data = {"message": "Se actualizo la categoria"}
            return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CategoryView(views.APIView):
    def get(self, request):
        queryset = Categoria.objects.all() # listado de objetos
        serializer = CategorySerializer(data=queryset, many=True)
        serializer.is_valid()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

'''class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductSerializer'''
   