from django.shortcuts import render

from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer
# Create your views here.


class ProductList(APIView):
    print('here')
    def get(self, request, format=None):
        bouncehouses = Product.objects.all()[0:]
        serializer = ProductSerializer(bouncehouses, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, collection_slug, product_slug):
        try:
            return Product.objects.filter(collection__slug=collection_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, collection_slug, product_slug, format=None):
        product = self.get_object(collection_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class ProductByCollection(APIView):
    def get_object(self, collection_slug):
        try:
            return Product.objects.filter(collection__slug=collection_slug)
        except Collection.DoesNotExist:
            raise Http404

    def get(self, request, collection_slug, format=None):
        product = self.get_object(collection_slug)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)