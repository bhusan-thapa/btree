"""testpro URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^$', 'home.views.index',name='index'),

    url(r'^subscription/$', 'home.views.subscription',name='subscription'),
	url(r'^accounts/register/$', TemplateView.as_view(template_name="registration/signup.html"), name='signup'),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
	url(r'^accounts/logout/$','django.contrib.auth.views.logout',{'next_page': '/'},name='logout'),

	url(r'^$','home.views.dashboard',name='dashboard'),

	url(r'^registraion/$','home.views.registraion',name='registraion'),

	url(r'^checkout$','home.views.checkout',name='checkout'),

	url(r'^payment$','home.views.payment',name='payment'),


	


	

	


	

     


    
]