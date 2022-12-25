from django.contrib import admin

from anasayfa.models import ayarlar,IletisimFormuMesaj


# Register your models here.
class ayarlarAdmin(admin.ModelAdmin):
    list_display = ['baslik','aciklama']
class IletisimFormuMesajAdmin(admin.ModelAdmin):
    list_display = ['isim','email','konu','mesaj_durumu']
    list_filter = ['mesaj_durumu']

admin.site.register(ayarlar, ayarlarAdmin)
admin.site.register(IletisimFormuMesaj,IletisimFormuMesajAdmin)