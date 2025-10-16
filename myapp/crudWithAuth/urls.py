from django.urls import path
from . import views
from . import user_view

urlpatterns = [
    path('register/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('home/', views.Home, name='home'),
    path('logout/', views.Logout, name='logout'),
    path('create/', user_view.create_portfolio, name='create_portfolio'),
    path('', user_view.preview, name='portfolio_preview'),
    # path('list/', views.list_users, name='list_users'),
    # path('edit/<uuid:id>/', views.edit_user, name='edit_user'),
    # path('delete/<uuid:id>/', views.delete_user, name='delete_user'),
    # path('view/<uuid:id>/', views.view_user, name='view_user'),



]
