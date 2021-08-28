"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.urls import  path,re_path
from . import views
# from fsspbotdb.views import  *
urlpatterns = [
    path("", views.index, name='index'),
    #path("set_webhook", views.set_webhook, name='set_webhook'),
    #path("HOOK-SyBPwfCLPl30", views.webhook, name='webhook'),
    #path("<slug:slug>", views.webhook, name='webhook'),
    #123


]
