from django.shortcuts import render
from appMy.models import Blog
from datetime import datetime

# Create your views here.
def indexPage(request):    
    context={}
    return render(request,'index.html',context)

def hakkimdaPage(request):
    context={}
    return render(request,'hakkimda.html',context)

def iletisimPage(request):
    import datetime
    if request.method=="POST":
        yazar=request.POST.get("yazar")
        konu=request.POST.get("konu")
        icerik=request.POST.get("icerik")
        date_now=datetime.datetime.now()
        blog=Blog(title=konu,text=icerik,author=yazar,date_now=date_now)
        blog.save()
        # print(yazar,konu,icerik,date_now)
    
    context={}
    return render(request,'iletisim.html',context)

def formPage(request):
        blog_list=Blog.objects.all()
        
        context={
            "blog_list":blog_list,
        }
        return render(request,'form.html',context)