from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    login_view, logout_view, register_view, list_books,
    LibraryDetailView, admin_view, librarian_view, member_view,
    add_book, edit_book, delete_book, home
)

urlpatterns = [
    # Authentication Views
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', register_view, name='register'),

    # Role-based Views
    path('admin-page/', admin_view, name='admin_view'),
    path('librarian-page/', librarian_view, name='librarian_view'),
    path('member-page/', member_view, name='member_view'),

    # Book Management Views (permission-protected)
    path('books/add/', add_book, name='add_book'),
    path('books/edit/', edit_book, name='edit_book'),
    path('books/delete/', delete_book, name='delete_book'),

    # Book Listing and Library Detail
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Homepage
    path('', home, name='home'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('admin-dashboard/', views.admin_view, name='admin_view'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_view'),
    path('member-dashboard/', views.member_view, name='member_view'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('admin-dashboard/', views.admin_view, name='admin_view'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_view'),
    path('member-dashboard/', views.member_view, name='member_view'),

    # ✅ Add Book Views
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
]

