from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    home,
    redirect_to_login,
    register_view,
    BlogLoginView,
    BlogLogoutView,
    profile_view,
    profile_edit_view,
)

urlpatterns = [
    # Posts CRUD (matching requirement)
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/', PostListView.as_view(), name='post_list'),

    # Authentication & profiles
    path("login/", BlogLoginView.as_view(), name="login"),
    path("logout/", BlogLogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
    path("profile/edit/", profile_edit_view, name="profile_edit"),

    # Homepage (only one root URL)
    path("", home, name="home"),
]