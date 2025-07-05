from django.contrib import admin
from .models import GroupForm, GroupMembership, GroupPost

# Register your models here.

admin.site.register(GroupForm)
admin.site.register(GroupMembership)
admin.site.register(GroupPost)