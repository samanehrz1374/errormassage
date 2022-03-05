from django.shortcuts import render
from .models import Author,Book
from . forms import BookFormSet
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_book(request):
    # author = request.user.profile
    # # books = Book.objects.filter(author=author)
    # # form = BookForm(request.POST or None)
    # formset= BookFormSet(request.POST or None)
    if request.method == 'GET':
        template_name = 'books/create_book.html'

        bookform = request.user.profile
        formset = BookFormSet(queryset=Author.objects.none())
    elif request.method == 'POST':
        bookform = request.user.profile
        formset = BookFormSet(request.POST)
        if  formset.is_valid():
            # first save this book, as its reference will be used in `Author`
            # book = bookform.save()
            for form in formset:
                # so that `book` instance can be attached.
                author = form.save(commit=False)
                author.author = bookform 
                author.save()
            return redirect("create-book")
    return render(request, template_name, {
        'bookform': bookform,
        'formset': formset,
    })

    # return render(request, "books/create_book.html", context)


def bookview(request,concert_id):
    formset= Book.objects.all()

    context = {
        # "form": form,
        # "author": author,
        # "books": books
        "formsett":formset,
        
    }

    return render(request, "books/book.html", context)
