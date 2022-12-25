from django .shortcuts import render
from anasayfa.models import ayarlar
# sayfada görünmesini istediğiniz görünümleri burada belirtttik
def anasayfayz(request): #videoda bu fonkun adı index
    Ayarlar=ayarlar.objects.get(pk=1)
    context={"Ayarlar":Ayarlar}
    return render(request,'profil_son.html',context)
