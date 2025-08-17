from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Post, Tag
from .models import Post
from .models import Comment
from taggit.forms import TagWidget

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "avatar"]

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Enter tags separated by commas")

    class Meta:
        class Meta:
            model = Post
            fields = ["title", "content", "tags"]   # ✅ include tags
            widgets = {
                "tags": TagWidget(),   # ✅ Tag input widget
            }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # Prepopulate tags when editing
            self.fields['tags'].initial = ", ".join(
                [tag.name for tag in self.instance.tags.all()]
            )

    def save(self, commit=True):
        instance = super().save(commit=False)
        tags_str = self.cleaned_data.get('tags', '')
        tag_names = [t.strip() for t in tags_str.split(",") if t.strip()]
        tag_objs = [Tag.objects.get_or_create(name=name)[0] for name in tag_names]

        if commit:
            instance.save()
            instance.tags.set(tag_objs)
        else:
            # Delay setting tags until instance is saved
            self._pending_tags = tag_objs
        return instance

    def save_m2m(self):
        """
        Ensure tags are saved properly even if save(commit=False) was used.
        """
        super().save_m2m()
        if hasattr(self, '_pending_tags'):
            self.instance.tags.set(self._pending_tags)
            
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment...'}),
        }