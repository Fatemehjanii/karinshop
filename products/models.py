from xml.dom.minidom import Comment

from django.db import models
from core.models import Base
from django.utils import timezone
import uuid
import os


def _get_image_path(obj,filename):
    now = timezone.now()
    base_path = 'products/'
    new_filename = str(uuid.uuid5(uuid.NAMESPACE_URL,obj.pk))
    ext = os.path.splitext(filename)[1]
    p = os.path.join(base_path, now.strftime('%Y/%m/%d'), f"{new_filename}{ext}")
    return p

class Product(Base):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True,default=uuid.uuid4)
    price = models.IntegerField(default=0)
    discount = models.FloatField(default=0)
    enabled = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(_get_image_path,null=True, blank=True)
    send_today = models.BooleanField(default=False)
    rating = models.FloatField(default=0)
    color_hex = models.CharField(max_length=255, default='#000000')



class Tag(Base):
    name = models.CharField(max_length=255)


class Comment(Base):
    name = models.CharField(max_length=255)

class Like(Base):
    pass

class Category(Base):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('Category',
                                on_delete=models.PROTECT,
                               related_name='childs',
                               null=True,
                               blank=True ,
                               default=None)

