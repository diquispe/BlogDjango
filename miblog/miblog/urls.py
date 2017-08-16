"""miblog URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
# importaciones para servir archivos estaticos, pegado desde la documentacion
# https://docs.djangoproject.com/en/1.11/howto/static-files/

from django.conf import settings
from django.conf.urls.static import static


from posts import views

#importamos todas las vistas de posts
#para llamarlo mas abajo
from posts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #importamos las urls de posts
    url(r'^posts/', include("posts.urls", namespace="posts")),
]

# agregamos las urlpatterns solo en modo DEBUG el cual concatena a las urls principales

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

