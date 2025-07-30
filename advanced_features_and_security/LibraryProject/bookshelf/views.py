from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm  # Make sure this form exists
from django.db import connection
from django.db.models import Q
from .forms import ExampleForm

# ========================
# Home View
# ========================
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Or another page
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})

def search_books(request):
    query = request.GET.get("q")
    results = Book.objects.filter(Q(title__icontains=query)) if query else []
    return render(request, 'bookshelf/book_list.html', {'results': results})


def get_books_by_title(title):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM bookshelf_book WHERE title = %s", [title])
        return cursor.fetchall()

def home(request):
    return HttpResponse("📚 Welcome to the Bookshelf App!")

# ========================
# View All Books
# ========================
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# ========================
# Create New Book
# ========================
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

# ========================
