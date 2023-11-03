from django.shortcuts import render
from .models import WebSiteSettings,About,Gallery,Menu,News

def LandingPage(request):
    home_data=WebSiteSettings.objects.all()
    about=About.objects.all()
    gallery=Gallery.objects.all()
    menu=Menu.objects.all()
    news=News.objects.filter()
    return render(request,'eatwell/index.html',{'data':home_data,'about':about,'gallery':gallery,'menu':menu,'news':news})
