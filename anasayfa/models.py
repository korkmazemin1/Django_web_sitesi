from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea

import paylasim.models


# Create your models here.
class ayarlar(models.Model):  # videodaki images
    STATUS = (
        ('TRUE', 'EVET'),
        ('FALSE', 'HAYIR'),
    )
    baslik = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    aciklama = models.CharField(max_length=255)
    sirket = models.CharField(max_length=150)
    adres = models.CharField(blank=True, max_length=150)
    telefon = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(max_length=50)
    smptserver = models.CharField(blank=True, max_length=150)
    smptppassword = models.CharField(blank=True, max_length=150)
    smtpeamil = models.CharField(blank=True, max_length=150)
    smtpport = models.CharField(blank=True, max_length=150)
    logo = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    hakkimizda = RichTextUploadingField(blank=True)
    iletisim = RichTextUploadingField(blank=True)
    referanslar = RichTextUploadingField(blank=True)
    durum = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.baslik)


class IletisimFormuMesaj(models.Model):
    STATUS = (
        ('YENİMESAJ', 'YENİMESAJ'),
        ('OKUNDU', 'OKUNDU')

    )
    email = models.CharField(blank=True, max_length=50, null=True)
    isminiz = models.CharField(blank=False, max_length=20, null=True)
    telefon_numarasi = models.CharField(blank=True, max_length=50)
    sorumlu = models.CharField(blank=False, max_length=50)
    konu = models.CharField(blank=True, max_length=20, null=True)
    isteme_tarihi = models.CharField(blank=True, max_length=20)
    mesaj = models.CharField(blank=True, max_length=200, null=True)
    bizi_nereden = models.CharField(blank=True, max_length=20)
    mesaj_durumu = models.CharField(max_length=10, choices=STATUS, default="YENİMESAJ", null=True)
    ip = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.isminiz


class IletisimFormu(ModelForm):
    class Meta:
        model = IletisimFormuMesaj
        fields = ['isminiz', 'konu', 'email', 'mesaj']
        widgets = {
            'isminiz': TextInput(attrs={'class': 'input', 'placeholder': 'İsim ve Soyisim'}),
            'konu': TextInput(attrs={'class': 'input', 'placeholder': 'Konu'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Email adresi'}),
            'mesaj': TextInput(attrs={'class': 'id', 'placeholder': 'Mesajınız', 'rows': 'S'})

        }


