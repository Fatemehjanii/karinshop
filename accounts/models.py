from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import uuid
import os

def _get_avatar_upload_path(instance, filename):
    now = timezone.now()
    base_path = 'avatars/'
    new_filename = str(uuid.uuid5(uuid.NAMESPACE_URL, instance.pk))
    ext = os.path.splitext(filename)[1]
    p = os.path.join(base_path, now.strftime('%Y/%m/%d'), f"{new_filename}{ext}")
    return p

class User(AbstractUser):
    username = None
    email = models.EmailField('email', unique=True)
    phone = models.CharField('phone', max_length=20, null=True, blank=True)
    address = models.CharField('address', max_length=100, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to=_get_avatar_upload_path, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"
