from django.urls import path
from . import views

urlpatterns = [
    path('', views.charts,name="charts"),
    path('db/', views.db),
]