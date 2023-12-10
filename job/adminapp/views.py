from django.contrib import messages
from django.shortcuts import render, redirect
from adminapp.models import cat
# Create your views here.


def web(request):
    return render(request, 'web.html')



def cats(request):
    if request.method == "POST":
        c = request.POST.get("Category")
        n = request.POST.get("Name")
        l = request.POST.get("Link")
        ln = request.POST.get("Linkname")
        s = request.POST.get("shotnot")
        l2 = request.POST.get("Link2")
        ln2 = request.POST.get("Linkname2")
        s2 = request.POST.get("shotnot2")
        l3 = request.POST.get("Link3")
        ln3 = request.POST.get("Linkname3")
        s3 = request.POST.get("shotnot3")


        d = request.POST.get("Details")
        IM = request.FILES["Image"]
        IM2 = request.FILES["Image2"]
        IM3 = request.FILES["Image3"]
        IM4 = request.FILES["Image4"]
        IM5 = request.FILES["Image5"]
        IM6 = request.FILES["Image6"]
        obj = cat(Category=c, Details=d,Link=l,Linkname=ln,
                  Link2=l2,Linkname2=ln2,Link3=l3,Linkname3=ln3,Name=n,Image=IM,Image2=IM2,Image3=IM3,
                  Image4=IM4,Image5=IM5,Image6=IM6,shotnot=s,shotnot2=s2,shotnot3=s3)
        obj.save()
        messages.success(request,"added Successfully")
    return redirect(web)



def table(request):
    data=cat.objects.all()
    return render(request, 'tables.html',{"data":data})



def deletecat(request, dataid):
    data=cat.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Delete Successfully")
    return redirect(table)