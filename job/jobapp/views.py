import random
from difflib import get_close_matches

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from adminapp.models import cat
from django.urls import reverse
from django.contrib import messages
import wikipediaapi

# Create your views here.
from adminapp.views import web


def home(request):
    return render(request,"home.html")
def login(request):
    return render(request,"login.html")
def cal(request):
    return render(request,"cal.html")

def search(request):
    query = request.GET.get('q')
    data = None
    datas = None
    if not query:
        data = None
        return redirect(home)

    elif query == "calculator":
        return redirect(cal)
    else:
        data=cat.objects.filter(Q(Name__icontains=query))
        datas=cat.objects.filter(Q(Category__icontains=query))
        if not data.exists() and not datas.exists():
            possible_names = [item.Name for item in cat.objects.all()]
            close_matches = get_close_matches(query, possible_names, n=3, cutoff=0.6)
            possible_name = [item.Category for item in cat.objects.all()]
            close_matche = get_close_matches(query, possible_name, n=3, cutoff=0.6)

            # You can adjust the parameters (n, cutoff) based on your needs

            # Optionally, you can perform another query using the close matches
            close_data = cat.objects.filter(Name__in=close_matches)
            close_dat = cat.objects.filter(Category__in=close_matche)

            return render(request, 'home.html', {'close_data': close_data,'close_dat': close_dat})


    return render(request, 'searchdetails.html', {"data":data,"datas":datas})


def retur(request, item_id):
    item = cat.objects.filter(id=item_id)
    return render(request, 'retur.html', {'item': item})


def Image(request,dataid):
    data = cat.objects.filter(id=dataid)
    return render(request,"Image.html",{"data":data})

def Image2(request,dataid):
    datas = cat.objects.filter(Category=dataid)
    images=[]
    for data in datas:
        images.extend([data.Image.url, data.Image2.url, data.Image3.url, data.Image4.url, data.Image5.url, data.Image6.url])
        random.shuffle(images)
        data.shuffled_images = images

    return render(request,"Image.html",{"datas":datas})

def catr(request, item_id):
    item = cat.objects.filter(Category=item_id)
    return render(request, 'cat.html', {'item': item})


def ret(request,dataid):
    data = cat.objects.filter(id=dataid)
    return render(request,"searchdetails.html",{"data":data})
def retcat(request,dataid):
    data = cat.objects.filter(Category=dataid)
    return render(request,"retcat.html",{"data":data})


def loginpage(request):
    return render(request,"loginadmin.html")


def logins(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username__contains=username).exists():
            user = authenticate(username=username, password=password)

        return redirect(web)
    else:
        return redirect(logins)


def adminlogout(request):
    return redirect(login)