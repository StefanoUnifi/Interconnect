from django.contrib import admin
from .models import Groups, GroupMembership, GroupPost

# Register your models here.

admin.site.register(Groups)
admin.site.register(GroupMembership)
admin.site.register(GroupPost)