from django .shortcuts import render

# sayfada görünmesini istediğiniz görünümleri burada belirtttik
def anasayfayz(request):
    text = "\n  Şuan anasayfadasınız \n "
    context={"text":text}
    return render(request,'index.html5.html',context)
