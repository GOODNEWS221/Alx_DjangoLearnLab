from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Registration endpoint
    path('login/', LoginView.as_view(), name='login'),           # Login endpoint
    path('profile/', ProfileView.as_view(), name='profile'),    # Profile management
]