from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    login_view, logout_view, register_view, list_books,
    LibraryDetailView, admin_view, librarian_view, member_view,
    add_book, edit_book, delete_book, home
)

urlpatterns = [
    # Authentication
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', register_view, name='register'),

    # Homepage
    path('', home, name='home'),

    # Role-based Access Views
    path('admin-page/', admin_view, name='admin_view'),
    path('librarian-page/', librarian_view, name='librarian_view'),
    path('member-page/', member_view, name='member_view'),

    # Book Management
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),

    # Book Listing & Library Detail
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
