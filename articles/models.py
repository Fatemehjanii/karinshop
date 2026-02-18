from django.db import models
from core.models import Base
from django.utils import timezone

def _get_image_path(obj,filename):
    now = timezone.now()
    base_path = 'articles/'
    new_filename = str(uuid.uuid5(uuid.NAMESPACE_URL,obj.pk))
    ext = os.path.splitext(filename)[1]
    p = os.path.join(base_path, now.strftime('%Y/%m/%d'), f"{new_filename}{ext}")
    return p

# Create your models here.
class Articles(Base):
     title = models.CharField(max_length=50)
     description = models.TextField(max_length=300)
     design = models.TextField(max_length=300)
     processor = models.CharField(max_length=50)
     rom = models.CharField(max_length=50)
     internal_memmory = models.CharField(max_length=50)
     battery = models.CharField(max_length=70)
     camera_performance = models.TextField(max_length=300)
     image = models.ImageField(_get_image_path, null=True, blank=True)
     category = models.ForeignKey('ArticleCat', on_delete=models.CASCADE)

     def __str__(self):
         return f"{self.title}"
     
class ArticleCat(Base):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class testmodel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)



