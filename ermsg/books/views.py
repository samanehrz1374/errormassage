from django.shortcuts import render
from .models import Author,Book
from . forms import BookFormSet
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

def create_book(request, pk):
    author = Author.objects.get(pk=pk)
    # books = Book.objects.filter(author=author)
    # form = BookForm(request.POST or None)
    formset= BookFormSet(request.POST or None)

    if request.method == "POST":
        if formset.is_valid():
            formset.instance = author
            # book = form.save(commit=False)
            # book.author = author
            formset.save()
            return redirect("create-book", pk=author.id)
        # else:
        #     return render(request, "partials/book_form.html", context={
        #         "form": form
        #     })

    context = {
        # "form": form,
        # "author": author,
        # "books": books
        "formset":formset,
        "author":author,
    }

    return render(request, "books/create_book.html", context)


def bookview(request,concert_id):
    formset= Book.objects.all()

    context = {
        # "form": form,
        # "author": author,
        # "books": books
        "formsett":formset,
        
    }

    return render(request, "books/book.html", context)
