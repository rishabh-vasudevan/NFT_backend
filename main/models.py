from django.db import models

# Create your models here.

class NFTData(models.Model):
    # key = models.CharField(max_length=200)
    # image_url = models.URLField(max_length=200)
    data = JSONField(null = True, blank = True)