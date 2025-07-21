from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Book, Library
from .forms import RegisterForm  # Use if you have a custom registration form
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

# Check if user is in Admin group
def is_admin(user):
    return user.groups.filter(name='Admin').exists()

# Admin-only view
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_dashboard.html')


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    return render(request, 'add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request):
    return render(request, 'edit_book.html')

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request):
    return render(request, 'delete_book.html')
# ========================
# Role Check Functions
# ========================
def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def is_librarian(user):
    return user.groups.filter(name='Librarian').exists()

def is_member(user):
    return user.groups.filter(name='Member').exists()

# ========================
# Dashboard Views
# ========================
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_dashboard.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_dashboard.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_dashboard.html')

# ========================
# Authentication Views
# ========================
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Change to RegisterForm if customized
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # or list_books
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# ========================
# Book & Library Views
# ========================
@login_required
def home_view(request):
    return render(request, 'relationship_app/home.html', {'user': request.user})

@login_required
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# ========================
# Permission-Based Views
# ========================
@permission_required('relationship_app.add_book')
def add_book(request):
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.change_book')
def edit_book(request):
    return render(request, 'relationship_app/edit_book.html')

@permission_required('relationship_app.delete_book')
def delete_book(request):
    return render(request, 'relationship_app/delete_book.html')

