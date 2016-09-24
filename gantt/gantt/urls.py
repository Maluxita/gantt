"""gantt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from actividades import views
from reportevial import views as views_reporte

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.hola, name='hola'),
    url(r'^saludo/(?P<name>[a-z]*)', views.saludo, name='saludo'),
    url(r'^protegida$', views.protegida, name='protegida'),
    url(r'^avisoauth$', views.avisoauth, name='avisoauth'),
    url(r'^reportevial$', views_reporte.reportevial, name='reporte'),
    url(r'^grafica$', views_reporte.grafica, name='grafica'),



]
