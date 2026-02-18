from django.shortcuts import render
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
# from rest_framework import viewsets
from rest_framework import pagination

from . import serializers
from django.shortcuts import get_object_or_404

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'page'

class ListArticlesView(APIView):
    def get(self, request):
        obj = models.Articles.objects.all()
        s = serializers.ArticleSerializers(obj, many=True)
        return Response(s.data)

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Articles.objects.all()
    pagination_class = CustomPagination
    serializer_class = serializers.ArticleSerializers


class TestViewSet(viewsets.ModelViewSet):
    queryset = models.Articles.objects.all()
    serializer_class=serializers.TestSerializers
    pagination_class=CustomPagination



