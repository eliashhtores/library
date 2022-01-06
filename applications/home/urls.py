from django.urls import path
from . import views

app_name = 'home_app'

urlpatterns = [
    path('panel', views.HomePage.as_view(), name='panel'),
    path('test', views.TestPage.as_view(), name='test'),
]
