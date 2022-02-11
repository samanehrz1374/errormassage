from django.contrib import admin

# Register your models here.
from .models import Author, Book


class BookInLineAdmin(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInLineAdmin]


admin.site.register(Author, AuthorAdmin)