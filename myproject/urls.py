"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('singleproperty1',views.singleproperty1),
    path('propertytypes', views.propertytypes),
    path('commercial', views.commercial),
    path('flats', views.flats),
    path('house', views.house),
    path('plots', views.plots),
    path('villa', views.villa),
    path('blogpage', views.blogpage),
    path('blog1', views.blog1),
    path('termcondition', views.termcondition),
    path('trends', views.trends),
    path('privacy', views.privacy),
    path('single', views.single),
    path('sanchislpendidpage', views.sanchislpendidpage),
    path('sanchiplatinumpark', views.sanchiplatinumpark),
    path('goldsquare', views.goldsquare),
    path('kanakghar', views.kanakghar),
    path('kanakresidency', views.kanakresidency),
    path('aishwaryam', views.aishwaryam),
    path('tulip', views.tulip),
    path('mandotprime', views.mandotprime),
    path('krativilla', views.krativilla),
]
