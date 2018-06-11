"""beathub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from mybeathub.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mybeathub/', include('mybeathub.urls')),	
    url(r'^accounts/login/$',login),
    url(r'^accounts/logout/$',logout),
    url(r'^contactus/$',contactus),
    url(r'^contactus2/$',contactus2),


    url(r'^index/001.html/$',index001),
    url(r'^index/001-1.html/$',index0011),
    url(r'^index/001-2.html/$',index0012),

    url(r'^index/002.html/$',index002),
    url(r'^index/002-1.html/$',index0021),
    url(r'^index/002-2.html/$',index0022),

    url(r'^index/003.html/$',index003),
    url(r'^index/003-1.html/$',index0031),
    url(r'^index/003-2.html/$',index0032),

    url(r'^index/004.html/$',index004),
    url(r'^index/005.html/$',index005),
    url(r'^index/$',index),
    url(r'^accounts/register/$',register),
    
]