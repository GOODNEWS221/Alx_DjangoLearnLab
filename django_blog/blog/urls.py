from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    # ... other views like register_view etc.
)
from .views import (
    home,
    redirect_to_login,          # 👈 add this
    register_view,
    BlogLoginView,
    BlogLogoutView,
    profile_view,
    profile_edit_view,
)

urlpatterns = [
    # Posts CRUD
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    # ... existing auth urls:
    # path('login/', ...),
    # path('logout/', ...),
    # path('register/', ...),
    # path('profile/', ...),    
    path("", redirect_to_login),
    path("", home, name="home"),   # 👈 empty path (homepage)
    path("login/", BlogLoginView.as_view(), name="login"),
    path("logout/", BlogLogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
    path("profile/edit/", profile_edit_view, name="profile_edit"),
]

