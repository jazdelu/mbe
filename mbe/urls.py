"""mbe URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from member import urls as member_urls
from collection import urls as collection_urls
from page import views as page_views
from mbe import views as mbe_views
from wish import urls as wish_urls
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include(member_urls)),
    url(r'^wish/', include(wish_urls)),
    url(r'^p/',include(collection_urls)),
    url(r'^$', mbe_views.home, name = 'Home' ),
    url(r'^index/$',mbe_views.home, name = 'Home'),
    url(r'^collection/', page_views.get_collection_page, name = 'The Collection' ),
    url(r'^mbe/', page_views.get_about_page, name = 'About Us' ),
]
