"""tafutaProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView #Redirect base url to a specific application
#use static() to serve static files during dev't only
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "TAFUTA ADMINISTRATION"
admin.site.site_title = "Administration Dashboard"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', include('accounts.urls')),
    path('documents/', include('lostdoc.urls')),
    path('', RedirectView.as_view(url='signup/', permanent = True)),
    path('accounts/', include("django.contrib.auth.urls")),
    path('registration/',include('django.contrib.auth.urls'))
    
]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
