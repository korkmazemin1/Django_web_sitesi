from django.db import models

# Create your models here.
class ayarlar(models.Model):# videodaki images
    STATUS = (
        ('TRUE', 'EVET'),
        ('FALSE', 'HAYIR'),
    )
    baslik=models.CharField(max_length=150)
    keywords=models.CharField(max_length=255)
    aciklama=models.CharField(max_length=255)
    sirket=models.CharField(max_length=150)
    adres=models.CharField(blank=True,max_length=150)
    telefon=models.CharField(blank=True,max_length=15)
    fax=models.CharField(blank=True,max_length=15)
    email=models.CharField(blank=True,max_length=50)
    smptserver=models.CharField(max_length=150)
    smptppassword=models.CharField(max_length=150)
    smtpeamil=models.CharField(max_length=150)
    smtpport=models.CharField(blank=True,max_length=150)
    logo=models.ImageField(blank=True,upload_to='images/')
    facebook=models.CharField(max_length=50)
    instagram=models.CharField(max_length=50)
    twitter=models.CharField(max_length=50)
    hakkimizda=models.TextField()
    referanslar=models.TextField()
    durum=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.baslik)