from django.shortcuts import render
from .serializer import ProductSerializer
from .models import *
# from rest_framework.decorators import APIView
# from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView

# class Productlistwiew(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
# class ProductCreatwiew(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class ProductDelete(DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
# class PtoductUpdate(UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
from rest_framework.viewsets import ModelViewSet

class ProductCrud(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    


