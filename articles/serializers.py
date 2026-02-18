from rest_framework import serializers
from . import models


class ArticleSerializers(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()
    class Meta:
        model = models.Articles
        fields = "__all__"
        # fields = ['title','created_date','image']
    def get_discount(self,obj):
        return "hfhgfh"


class TestSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.testmodel
        fields ="__all__"