
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_user, name='create_user'),
    path('list/', views.list_users, name='list_users'),
    path('edit/<uuid:id>/', views.edit_user, name='edit_user'),
    path('delete/<uuid:id>/', views.delete_user, name='delete_user'),
    path('view/<uuid:id>/', views.view_user, name='view_user'),



]
