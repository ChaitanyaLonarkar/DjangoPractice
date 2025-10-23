from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
  path('todos/', views.TodoCreateListView.as_view(), name='todo-list'),
  path('todos/create/', views.TodoCreateListView.as_view(), name='todo-create'),
  path('todos/<int:pk>/', views.TodoCrudView.as_view(), name='todo-detail'),
  path('todos/<int:pk>/update/', views.TodoCrudView.as_view(), name='todo-update'),
  path('todos/<int:pk>/delete/', views.TodoCrudView.as_view(), name='todo-delete'),
  


]
