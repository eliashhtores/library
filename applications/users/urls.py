from django.urls import path
from . import views


app_name = 'users_app'

urlpatterns = [
    path('users/register', views.UserRegisterView.as_view(), name='register'),
    path('users/login', views.LoginView.as_view(), name='login'),
    path('users/logout', views.LogOutView.as_view(), name='logout'),
    path('users/update_password',
         views.UpdatePasswordView.as_view(), name='update_password'),
]
