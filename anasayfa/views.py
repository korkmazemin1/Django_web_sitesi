from django .shortcuts import render
from anasayfa.models import ayarlar
# sayfada görünmesini istediğiniz görünümleri burada belirtttik
def anasayfayz(request): #videoda bu fonkun adı index
    Ayarlar=ayarlar.objects.get(pk=1)
    context={"Ayarlar":Ayarlar}
    return render(request,'profil_son.html',context)
def hakkimizda(request):
    Ayarlar=ayarlar.objects.get(pk=1)
    context={"Ayarlar":Ayarlar}#  buraya ileride hangi listeyi koymak istersen onu koyarsın
    return render(request,'hakkimizda_son.html',context)
def iletisim(request):
    if request.method=="POST":
        form=IletisimFormu(request.POST)
        if form.is_valid():

    Ayarlar = ayarlar.objects.get(pk=1)
    context = {"Ayarlar": Ayarlar}  # buraya ileride hangi listeyi koymak istersen onu koyarsın
    return render(request, 'iletisim_son.html', context)