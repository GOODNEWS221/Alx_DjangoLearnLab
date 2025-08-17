from django.urls import path
from .views import (
    PostByTagListView,
    CommentCreateView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentUpdateView, CommentDeleteView,
    home, posts_by_tag, search_posts,
    register_view, BlogLoginView, BlogLogoutView,
    profile_view, profile_edit_view
)

urlpatterns = [
    # Posts CRUD
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/', PostListView.as_view(), name='post_list'),

    # Tags
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="posts_by_tag"),
    path("tags/<str:tag_name>/", posts_by_tag, name="posts_by_tag"),  # ⚠️ duplication here

    # Search
    path("search/", search_posts, name="search_posts"),

    # Comments CRUD
    path("posts/<int:post_id>/comments/new/", CommentCreateView.as_view(), name='add_comment'),
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name='comment_create'),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name='comment_update'),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name='comment_delete'),

    # Authentication & profiles
    path("login/", BlogLoginView.as_view(), name="login"),
    path("logout/", BlogLogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
    path("profile/edit/", profile_edit_view, name="profile_edit"),

    # Homepage
    path("", home, name="home"),
]


