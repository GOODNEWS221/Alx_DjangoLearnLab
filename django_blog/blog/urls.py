from django.urls import path
from .views import (
    CommentCreateView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentUpdateView, CommentDeleteView, add_comment,   # ✅ Added comment views
    home,
    redirect_to_login,
    register_view,
    BlogLoginView,
    BlogLogoutView,
    profile_view,
    profile_edit_view,
)

urlpatterns = [
    # Posts CRUD
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/', PostListView.as_view(), name='post_list'),

    # Comments CRUD
    path("posts/<int:post_id>/comments/new/", CommentCreateView.as_view(), name='add_comment'),
    path("post/<int:pk>/comments/new/", add_comment, name='add_comment'),  # ✅ use pk for consistency
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name='comment_update'),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name='comment_delete'),

    # Authentication & profiles
    path("login/", BlogLoginView.as_view(), name="login"),
    path("logout/", BlogLogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
    path("profile/edit/", profile_edit_view, name="profile_edit"),

    # Homepage
    path("", home, name="home"),
]


