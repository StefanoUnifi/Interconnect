from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class CommentsAdmin(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('pk', 'create_date', 'update_date')
    exclude = ('likes',)
    inlines = [
        CommentsAdmin,
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)