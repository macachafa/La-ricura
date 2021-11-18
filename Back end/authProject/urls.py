"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authApp import views
from authApp.views import inventario
from authApp.views.inventario import CategoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('productsList/', views.ProductListView.as_view()),
    path('productsAll/', views.ProductView.as_view()),
    path('productsCreate/', views.ProductCreate.as_view()),
    path('suppliersList/', views.SupplierView.as_view()),
    path('suppliersCreate/', views.SupplierCreate.as_view()),
    #path('products/', views.ProductListCreateView.as_view()),
    path('categoryCreate/', views.CategoryCreate.as_view()),
    path('categoryList/', views.inventario.CategoryView.as_view()),
    path('productsupdate/<int:pk>/', views.inventario.ProductActualizar.as_view()),
    path('suppliersupdate/<int:pk>/', views.inventario.SupplierActualizar.as_view()),
    path('categoryupdate/<int:pk>/', views.inventario.CategoryActualizar.as_view())
 
]
