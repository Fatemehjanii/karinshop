from django.shortcuts import render
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from . import serializers
from django.shortcuts import get_object_or_404

class ListArticlesView(APIView):
    def get(self, request):
        obj = models.Articles.objects.all()
        s = serializers.ArticleSerializers(obj, many=True)
        return Response(s.data)

class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        q = models.Articles.objects.all()
        s = serializers.ArticleSerializer(obj, many=True)
        return Response(s.data)

    def retrive(self, request, pk=None):
        q = models.Articles.objects.all()
        user = get_object_or_404(request, pk=pk)
        s = serializers.ArticleSerializer(user)
        return Response(s.data)