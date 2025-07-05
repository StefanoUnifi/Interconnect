from django.urls import path, include
from .views import (
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView,
    like_post,
    CommentCreateView,
    CommentDeleteView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<str:author>/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/<str:author>/<int:pk>/edit', PostUpdateView.as_view(), name='post-edit'),
    path('post/<str:author>/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('like/<int:pk>/', like_post, name='like-post'),
    path('comment/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<str:author>/<int:pk>/delete', CommentDeleteView.as_view(), name='comment-delete'),
]