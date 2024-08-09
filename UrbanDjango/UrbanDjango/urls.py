"""
URL configuration for UrbanDjango project.

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
from task2.views import task2_func
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', task2_func),
    path('class/', TemplateView.as_view(template_name='second_task/class_template.html')),
    path('platform/', TemplateView.as_view(template_name='third_task/platform.html')),
    path('platform/games/', TemplateView.as_view(template_name='third_task/games.html')),
    path('platform/cart/', TemplateView.as_view(template_name='third_task/cart.html')),
]
