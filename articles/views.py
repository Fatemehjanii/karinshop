from django.shortcuts import render
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers


class ListArticlesView(APIView):
    def get(self, request):
        obj = models.Articles.objects.all()
        s = serializers.ArticleSerializers(obj, many=True)
        return Response(s.data)