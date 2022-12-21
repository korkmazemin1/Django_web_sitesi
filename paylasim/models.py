from django.db import models

class kullanici(models.Model):
  kullaniciadi = models.CharField(max_length=255)
  foto=models.ImageField(blank=True,upload_to='images/')
