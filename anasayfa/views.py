from django.contrib import messages
from django .shortcuts import render


from anasayfa.models import ayarlar, IletisimFormu, IletisimFormuMesaj
from paylasim.models import fotiler


# sayfada görünmesini istediğiniz görünümleri burada belirtttik
def anasayfayz(request): #videoda bu fonkun adı index
    Ayarlar=ayarlar.objects.get(pk=1)
    sliderdata=fotiler.objects.all()[:100]
    context={"Ayarlar":Ayarlar,"sliderdata":sliderdata}
    return render(request,'anasayfa.html',context)
def hakkimizda(request):
    Ayarlar=ayarlar.objects.get(pk=1)
    context ={"Ayarlar" :Ayarlar} #  buraya ileride hangi listeyi koymak istersen onu koyarsın
    return render(request ,'hakkimizda_son.html' ,context)
def iletisim(request):
    if request.method=='POST':
        form=IletisimFormu(request.POST)
        if form.is_valid():
            data = IletisimFormuMesaj()
            data.isminiz= form.cleaned_data['isminiz']
            data.email = form.cleaned_data['email']
            data.konu = form.cleaned_data['konu']
            data.ip =request.META.get('REMOTE_ADDR')
            data.mesaj = form.cleaned_data['mesaj']
            data.save()
            messages.success(request,"Mesajınız başarılı bir şekilde gönderilmiştir teşekkürler")


    Ayarlar = ayarlar.objects.get(pk=1)
    form=IletisimFormu()
    context = {'Ayarlar':Ayarlar,'form':form}  # buraya ileride hangi listeyi koymak istersen onu koyarsın
    return render(request, 'iletisim_son.html', context)
