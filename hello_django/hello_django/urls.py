"""
URL configuration for hello_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('hello/', views.hello)
    #path('hello/<nome>', views.hello)
    #path('hello/<nome>/<int:idade>', views.hello)
    path('sum/<int:algarism1>/<int:algarism2>', views.sum),
    path('multiplication/<int:algarism1>/<int:algarism2>', views.multiplication),
    path('dividing/<int:algarism1>/<int:algarism2>', views.dividing),
    path('subtraction/<int:algarism1>/<int:algarism2>', views.subtraction)

]
