from django .shortcuts import render

# sayfada görünmesini istediğiniz görünümleri burada belirtttik
def paylasimyz(request):
    text = "\n  Şuan paylasım sayfasındasınız \n "
    context={"text":text}
    return render(request,'paylasim.html',context)
