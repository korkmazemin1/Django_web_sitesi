from django.contrib import admin

# Register your models here.
from paylasim.models import kullanici, fotiler

class kullaniciFotiInline(admin.TabularInline):
    model= fotiler
    extra = 3
class PaylasimAdmin(admin.ModelAdmin):
    list_display = ['kullaniciadi','soyadi']
    inlines = [kullaniciFotiInline]
class PaylasimFoti(admin.ModelAdmin): #admin panelindeki liste de hangi bilginin gösterilmesini istiyorsak onu belirtiyoruz. burada sahibi kısmını seçmişiz
    list_display = ["sahibi","foti_tag"]

admin.site.register(kullanici,PaylasimAdmin)
admin.site.register(fotiler,PaylasimFoti)