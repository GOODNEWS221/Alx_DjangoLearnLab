from django.urls import path
from .views import RegisterView, LoginView, ProfileView
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Registration endpoint
    path('login/', LoginView.as_view(), name='login'),           # Login endpoint
    path('profile/', ProfileView.as_view(), name='profile'),    # Profile management
]


urlpatterns += [
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]