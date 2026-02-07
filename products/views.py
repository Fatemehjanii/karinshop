from django.views import View
from django.shortcuts import render
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers

class ProductsDetails(View):
    def get(self, request):
        data_product_details = models.Product.objects.all()
        return render(request, 'products/product-details.html', {'data_product_details': data_product_details})

class ListProductView(APIView):
    def get(self, request, format=None ):
        obj = models.Product.objects.all()
        s = serializers.ProductListSerializer(obj, many=True )
        return Response(s.data)