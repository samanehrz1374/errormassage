from xml.etree.ElementInclude import include
import django
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('model/',include('ermsgg.urls')),
    path('books/',include('books.urls')),
    path('charts/',include('charts.urls')),
]
