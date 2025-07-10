from django.urls import path
from . import views

urlpatterns = [
    path('', views.GroupView.as_view(), name='group_list'),
    path('<int:group_id>/', views.GroupDetailView.as_view(), name='group_detail'),
    path('<int:group_id>/post/', views.CreateGroupPostView.as_view(), name='create_post'),
    path('<int:group_id>/post/<int:post_id>/delete/', views.DeleteGroupPostView.as_view(), name='delete_post'),
    path('<int:group_id>/remove_user/<int:user_id>/', views.RemoveUserView.as_view(), name='remove_user'),
    path('<int:group_id>/join/', views.GroupJoinView.as_view(), name='join_group'),
    path('<int:group_id>/leave/', views.GroupLeaveView.as_view(), name='leave_group'),
    path('create/', views.CreateGroupView.as_view(), name='group_create'),
]