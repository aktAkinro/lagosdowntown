from django.conf import settings
from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class LikedItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # the three fields below are necessary for a generic relationship
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) #content type is used to create generic relationships
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
