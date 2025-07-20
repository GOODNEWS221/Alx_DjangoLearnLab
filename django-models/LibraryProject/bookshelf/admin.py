from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Shows these fields in list view
    list_filter = ('author', 'publication_year')  # Adds filters in sidebar
    search_fields = ('title', 'author')  # Adds search bar for title and authorfrom django.contrib import admin

# Register your models here.
