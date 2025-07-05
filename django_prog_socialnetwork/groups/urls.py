from django.urls import path
from . import views

urlpatterns = [
    path('', views.group_list, name='group_list'),
    path('<int:group_id>/', views.group_detail, name='group_detail'),
    path('<int:group_id>/post/', views.create_post, name='create_post'),
    path('/post/<int:post_id>/delete/', views.delete_post, name='delete_post'),

    path('<int:group_id>/remove_user/<int:user_id>/', views.remove_user, name='remove_user'),
]