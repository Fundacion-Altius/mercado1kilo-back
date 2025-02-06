from django.urls import path
from .views import (
    register, login, user_list_create, user_detail, group_list,
    group_create, user_assign_group, activity_list, activity_detail
)

urlpatterns = [
    # User-related endpoints
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('users/', user_list_create, name='user-list-create'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('users/<int:pk>/assign-group/', user_assign_group, name='user-assign-group'),

    # Group-related endpoints
    path('groups/', group_list, name='group-list'),
    path('groups/create/', group_create, name='group-create'),

    # Activity-related endpoints
    path('activities/', activity_list, name='activity-list'),
    path('activities/<int:pk>/', activity_detail, name='activity-detail'),
]