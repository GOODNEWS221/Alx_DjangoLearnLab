from django.urls import path
from .views import (
    register_view,
    BlogLoginView,
    BlogLogoutView,
    profile_view,
    profile_edit_view,
)

urlpatterns = [
    path("login/", BlogLoginView.as_view(), name="login"),
    path("logout/", BlogLogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
    path("profile/edit/", profile_edit_view, name="profile_edit"),
]

