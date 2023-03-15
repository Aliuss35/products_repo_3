from os import stat
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework.decorators import api_view
from rest_framework import status





# Create your views here.
@api_view(['GET', 'POST'])
def get_all_products(request):
  if request.method == 'GET':
    all_products = Product.objects.all()
    serializer = ProductSerializer(all_products, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    
    return Response(serializer.data, status= status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def product_by_id(request,pk):
  products = get_object_or_404(Product, pk=pk)
  if request.method == 'PUT':
    serializer= ProductSerializer(products, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  elif request.method == 'GET':
    serializer=ProductSerializer(products)
    return Response(serializer.data)
  elif request.method == 'DELETE':
    products.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)