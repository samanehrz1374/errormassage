from django.contrib import admin
from django.urls import path
from . import views
from books.views import create_book,bookview


urlpatterns = [
    path('',  create_book, name='create-book'),
    path('books/<concert_id>',bookview)
]