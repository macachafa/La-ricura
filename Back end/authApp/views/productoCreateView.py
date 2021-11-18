from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authApp.serializers.productoserilizer import ProductSerializer

class ProductListView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        tokenData = {"Nombre":request.data["Nombre"],
        "Unidad de Medida":request.data["Unidad de Medida"],
        "Stock":request.data["Stock"],
        "Categoria":request.data["Categoria"],
        "Proveedor":request.data["Proveedor"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)