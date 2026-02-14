from rest_framework import serializers
from . import models


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Articles
        fields = ['title','created_date','image']