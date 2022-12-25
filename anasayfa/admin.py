from django.contrib import admin

from anasayfa.models import ayarlar


# Register your models here.
class ayarlarAdmin(admin.ModelAdmin):
    list_display = ['baslik','aciklama']


admin.site.register(ayarlar, ayarlarAdmin)