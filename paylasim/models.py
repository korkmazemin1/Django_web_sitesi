from django.db import models


class kullanici(models.Model):
    STATUS = (
      ('TRUE','EVET'),
      ('FALSE', 'HAYIR'),
    )
    soyadi = models.CharField(max_length=30,blank=True,null=True,default="kimse")
    kullaniciadi = models.CharField(max_length=255)
    foto = models.ImageField(blank=True, upload_to='images/')
    ebeveyn= models.ForeignKey('self',blank=True,null=True,related_name='çocuk',on_delete=models.CASCADE)


class fotiler(models.Model):
    STATUS = (
        ('TRUE', 'EVET'),
        ('FALSE', 'HAYIR'),
    )
    sahibi =models.ForeignKey(kullanici,on_delete=models.CASCADE)
    foti= models.ImageField(blank=True,upload_to='images/')# images olarak uploada kaydoldu ,eğer sınıflandırılmak istenirse images yazan yerde nereye lazımsa o şekilde yazabilirsin