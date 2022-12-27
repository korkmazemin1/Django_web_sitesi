from django .shortcuts import render

from paylasim.models import fotiyukle, fotiler


# sayfada görünmesini istediğiniz görünümleri burada belirtttik
def paylasimyz(request):
    text = "\n  Şuan paylasım sayfasındasınız \n "
    context={"text":text}
    return render(request,'paylasim.html',context)
def fotimiyukle(request):
    if request.method=='POST':
        form=fotiyukle(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,"profil.html",{"obj":obj})
    else:
            form=fotiyukle()
            img=fotiler.objects.all
            return render(request,"profil.html",{"img":img,"form":form})

