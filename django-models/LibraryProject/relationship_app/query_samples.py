import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Librarian, Library

# Sample query using ForeignKey relation
# Let's assume you already have a Library with ID 1
try:
    librarian = Librarian.objects.get(library=1)
    print(librarian.name)
except Librarian.DoesNotExist:
    print("Librarian not found for library with ID 1")
    
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

# Sample usage (run with `python query_samples.py`)
if __name__ == "__main__":
    print("Books by Author 'John Doe':")
    for book in books_by_author('John Doe'):
        print(f"- {book.title}")

    print("\nBooks in Library 'Central Library':")
    for book in books_in_library('Central Library'):
        print(f"- {book.title}")

    print("\nLibrarian of 'Central Library':")
    print(get_librarian_for_library('Central Library'))
