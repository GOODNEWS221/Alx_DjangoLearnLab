from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created! You can now log in.")
            # Optionally auto-login:
            # login(request, user)
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})

class BlogLoginView(LoginView):
    template_name = "registration/login.html"   # Django expects registration/ by default

class BlogLogoutView(LogoutView):
    next_page = reverse_lazy("login")

@login_required
def profile_view(request):
    return render(request, "blog/profile.html")

@login_required
def profile_edit_view(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, "blog/profile_edit.html", {"u_form": u_form, "p_form": p_form})