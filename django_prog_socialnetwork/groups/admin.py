from django.contrib import admin
from .models import CustomGroup, GroupMembership, GroupPost

# Register your models here.


class GroupFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)
    filter_horizontal = ('members','moderators',)

class GroupPostAdmin(admin.ModelAdmin):
    list_display = ('group', 'author', 'content', 'created_at')
    search_fields =  ('content','author__username', 'group__name')
    list_filter = ('group', 'author')
    ordering = ('-created_at')

class GroupMembershipAdmin(admin.ModelAdmin):
    list_display = ('group', 'user', 'is_moderator')
    list_filter = ('is_moderator', 'group')
    search_fields = ('user__username', 'group__name')