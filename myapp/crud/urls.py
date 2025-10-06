
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_user, name='create_user'),
    path('list/', views.list_users, name='list_users'),
    path('edit/<int:user_index>/', views.edit_user, name='edit_user'),


]
