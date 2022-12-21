from django.contrib import admin

# Register your models here.
from paylasim.models import kullanici, fotiler


class PaylasimAdmin(admin.ModelAdmin):
    list_display = ['kullaniciadi','soyadi']
class PaylasimFoti(admin.ModelAdmin):
    list_display = ["sahibi"]

admin.site.register(kullanici,PaylasimAdmin)
admin.site.register(fotiler,PaylasimFoti)