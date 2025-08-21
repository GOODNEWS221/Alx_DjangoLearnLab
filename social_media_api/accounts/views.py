from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserProfileSerializer

User = get_user_model()

# -------------------------------
# Registration View
# -------------------------------
class RegisterView(generics.CreateAPIView):
    """
    Endpoint for registering a new user.
    Returns auth token upon successful registration.
    """
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

# -------------------------------
# Login View
# -------------------------------
class LoginView(APIView):
    """
    Endpoint for user login.
    Returns auth token upon successful login.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=400)

# -------------------------------
# Profile View
# -------------------------------
class ProfileView(generics.RetrieveUpdateAPIView):
    """
    GET: Retrieve the authenticated user's profile
    PUT/PATCH: Update the authenticated user's profile
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Return the currently authenticated user
        return self.request.user
