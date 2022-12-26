from django.db import models
from django.utils.safestring import mark_safe


class kullanici(models.Model):# videodaki product
    STATUS = (
      ('TRUE','EVET'),
      ('FALSE', 'HAYIR'),
    )
    soyadi = models.CharField(max_length=30,blank=True,null=True,default="kimse")
    kullaniciadi = models.CharField(max_length=255)
    foto = models.ImageField(blank=True, upload_to='images/')
    ebeveyn = models.ForeignKey('self',blank=True,null=True,related_name='çocuk',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.kullaniciadi) # burada isim kısmında ne dönmesi gerektiğini belirttik

class fotiler(models.Model):# videodaki images
    STATUS = (
        ('TRUE', 'EVET'),
        ('FALSE', 'HAYIR'),
    )
    baslik=models.CharField(max_length=54,blank=True,null=True)
    sahibi =models.ForeignKey(kullanici,on_delete=models.CASCADE)# kullanıcı sınıfından bir obje ebevyni oldu(parent)
    foti= models.ImageField(blank=True,upload_to='images/')# images olarak uploada kaydoldu ,eğer sınıflandırılmak istenirse images yazan yerde nereye lazımsa o şekilde yazabilirsin
    aciklama= models.CharField(max_length=54,blank=True,null=True)
    slug = models.SlugField(blank=True,max_length=200)
    def __str__(self):
         full_path=[self.baslik]
         k=self.sahibi
         while k is not None:
             full_path.append(k.kullaniciadi)
             k = k.sahibi
         return '>>'.join(full_path[::-1])



    def foti_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.foti.url))
    foti_tag.short_description= "gönderi"