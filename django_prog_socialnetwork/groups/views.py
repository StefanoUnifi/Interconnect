from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, CreateView, DeleteView
from django.contrib import messages
from django.views import View
from .forms import GroupForm
from .models import CustomGroup, GroupPost, GroupMembership
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class GroupView(LoginRequiredMixin, View):
    def get(self, request):
        groups = CustomGroup.objects.all()
        return render(request, 'groups/group_list.html', {'groups': groups})

class GroupDetailView(LoginRequiredMixin, DetailView):
    def get(self, request, group_id):
        group = get_object_or_404(CustomGroup, id=group_id)
        posts = group.posts.all()
        is_member = GroupMembership.objects.filter(group=group, user=request.user).exists()
        is_moderator = group.is_moderator(request.user)
        return render(
            request, 'groups/group_detail.html', {
                'group': group,
                'posts': posts,
                'is_member': is_member,
                'is_moderator': is_moderator
            }
        )

class GroupJoinView(LoginRequiredMixin, View):
    def post(request, group_id):
        group = get_object_or_404(CustomGroup, id=group_id)
        GroupMembership.objects.get_or_create(group=group, user=request.user)

        messages.success(request, f'Ti sei unito al gruppo {group.name}.')
        return redirect('group_detail', group_id=group.id)

class GroupLeaveView(LoginRequiredMixin, View):
    def post(self, request, group_id):
        group = get_object_or_404(CustomGroup, id=group_id)
        GroupMembership.objects.filter(group=group, user=request.user).delete()

        messages.success(request, f'Hai lasciato il gruppo {group.name}.')
        return redirect('group_list')

class CreateGroupPostView(LoginRequiredMixin, CreateView):
    def post(self, request, group_id):
        group = get_object_or_404(CustomGroup, id=group_id)
        if not GroupMembership.objects.filter(group=group, user=request.user).exists():
            messages.error(request, 'Non fai parte di questo gruppo.')
            return redirect('group_detail', group_id=group.id)

        content = request.POST.get('content')
        if content:
            GroupPost.objects.create(group=group, author=request.user, content=content)
            messages.success(request, 'Post creato con successo.')
        return redirect('group_detail', group_id=group.id)

class DeleteGroupPostView(LoginRequiredMixin, DeleteView):
    def post(self, request, group_id, post_id):
        post = get_object_or_404(GroupPost, id=post_id)
        group = post.group

        if request.user == post.author or group.is_moderator(request.user):
            post.delete()
            messages.success(request, 'Post eliminato.')
        else:
            messages.error(request, 'Non hai i permessi per eliminare questo post.')

        return redirect('group_detail', group_id=group.id)

class RemoveUserView(LoginRequiredMixin, DeleteView):
    def post(self, request, group_id, user_id):
        group = get_object_or_404(CustomGroup, id=group_id)
        user_to_remove = get_object_or_404(User, id=user_id)

        if not group.is_moderator(request.user):
            messages.error(request, 'Non hai i permessi per rimuovere utenti da questo gruppo.')
            return redirect('group_detail', group_id=group.id)

        GroupMembership.objects.filter(group=group, user=user_to_remove).delete()
        messages.success(request, f'{user_to_remove.username} è stato rimosso dal gruppo.')
        return redirect('group_detail', group_id=group.id)


class CreateGroupView(LoginRequiredMixin, CreateView):
    model = CustomGroup
    fields = GroupForm
    template_name = 'groups/group_create.html'

    def form_valid(self, form):
        group = form.save(commit=False)
        group.created_by = self.request.user
        group.save()
        form.save_m2m()
        GroupMembership.objects.create(group=group, user=self.request.user, role='moderator')
        messages.success(self.request, 'Gruppo creato con successo.')
        return redirect('group_detail', group_id=group.id)