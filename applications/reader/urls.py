from django.urls import path
from . import views

app_name = 'reader_app'

urlpatterns = [
    path('reader/loan/register/', views.RegisterLoan.as_view(), name='loan_register'),
    path('reader/loan/invalid/', views.InvalidLoan.as_view(), name='invalid'),
    # path('reader/loan/list', views.ListLoan.as_view(), name='loan_list'),
]
