from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import redirect
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post
from .forms import PostForm
from .models import Post, Comment
from .forms import CommentForm

from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm


def redirect_to_login(request):
    return redirect("login")

def home(request):
    return render(request, "blog/home.html")

# List view — public
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 10
    ordering = ['-published_date']

# Detail view — public
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

# Create view — only for authenticated users
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        # set the author automatically
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

# Update view — only author can update
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

# Delete view — only author can delete
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

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


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return redirect('post_detail', pk=post.pk)


@method_decorator(login_required, name='dispatch')
class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def get_queryset(self):
        # Only allow author to edit their comment
        return super().get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})


@method_decorator(login_required, name='dispatch')
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_queryset(self):
        # Only allow author to delete their comment
        return super().get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})