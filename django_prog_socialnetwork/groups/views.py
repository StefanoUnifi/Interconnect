from django.shortcuts import render, get_object_or_404, redirect
from openpyxl.pivot.cache import GroupMember
from django.contrib import messages
from .models import GroupForm, GroupPost, GroupMembership
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def group_list(LoginRequiredMixin, request):
    groups = GroupForm.objects.all()
    return render(request, 'groups/group_list.html'), {'groups': groups}

def group_detail(LoginRequiredMixin, request, group_id):
    group = get_object_or_404(GroupForm, id=group_id)
    posts = group.posts.all()
    return render(request, 'groups/group_detail.html', {'group': group, 'posts': group.posts})

def create_post(LoginRequiredMixin, request, group_id):
    group = get_object_or_404(GroupForm, id=group_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            GroupPost.objects.create(group=group, author=request.user,content=content)
        return redirect('group_detail', group_id=group.id)

    return render(request, 'groups/create_post.html', {'group': group})

def delete_post(LoginRequiredMixin, request, group_id):
    post = get_object_or_404(GroupForm, id=group_id)
    membership = GroupMember.objects.filter(group=post.group, user=request.user, is_moderator=True).first()

    if request.user == post.author or membership:
        post.delete()
        messages.success(request, 'Post eliminato.')
    return redirect('group_detail', group_id=post.group.id)

def remove_user(LoginRequiredMixin, request, group_id, user_id):
    group = get_object_or_404(GroupForm, id=group_id)
    membership = GroupMember.objects.filter(group=group, user=request.user, is_moderator=True).first()

    if membership:
        GroupMembership.objects.filter(group=group, user=request.user, is_moderator=True).delete()
        messages.success(request, 'Utente rimosso dal gruppo.')

    return redirect('group_detail', group_id=group.id)