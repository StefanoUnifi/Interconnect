from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, View, ListView, UpdateView, CreateView
from .forms import CustomUserCreationForm
from .models import CustomUser, UserFollowing
from .forms import UserProfileEdit
from posts.models import Post
from posts.forms import CommentForm

# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class UserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        posts = Post.objects.filter(author=user)
        post_count = posts.count()
        followers_count = UserFollowing.objects.filter(following_user_id=user).count()
        following_count = UserFollowing.objects.filter(user_id=user).count()

        # Check if the current user is following the user being viewed
        is_following = UserFollowing.objects.filter(
            user_id=self.request.user, following_user_id=user
        ).exists()

        context['posts'] = posts
        context['post_count'] = post_count
        context['followers_count'] = followers_count
        context['following_count'] = following_count
        context['is_following'] = is_following
        context['form_comment'] = CommentForm()

        return context


class FollowToggleView(View):
    def post(self, request, pk, *args, **kwargs):
        user_to_follow = get_object_or_404(CustomUser, pk=pk)

        action = request.POST.get('action')

        if action == 'follow':
            UserFollowing.objects.create(
                user_id=request.user, following_user_id=user_to_follow
            )
        elif action == 'unfollow':
            UserFollowing.objects.filter(
                user_id=request.user, following_user_id=user_to_follow
            ).delete()

        next_page = request.POST.get('next_page', '/')
        return redirect(next_page)


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return (
            super().get_queryset().order_by('username').exclude(pk=self.request.user.pk)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        following = UserFollowing.objects.filter(user_id=user).values_list(
            'following_user_id__pk', flat=True
        )

        context['following'] = following
        return context


class ChangeUserProfile(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'user_change.html'
    form_class = UserProfileEdit

    def get_success_url(self):
        return reverse_lazy('user_profile', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        return self.request.user