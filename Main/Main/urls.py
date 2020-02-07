"""Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.contrib import admin
from django.urls import path, include
#download lib for handling static files 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static



from Home.views import home_view, contact_view, ciriculum_vitae_view, socai_media

urlpatterns = [
    path("admin/", admin.site.urls), 
    path("", include("Home.urls")),
    path("contact/", contact_view),
    path("food/", include("Food.urls")),
    path("user/", include("User.urls")),
    path("articles/", include("Articles.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #Works just for Debug mod when prefixes are local
else:
    pass
    #https://docs.djangoproject.com/en/3.0/howto/static-files/deployment/    

urlpatterns += staticfiles_urlpatterns()

