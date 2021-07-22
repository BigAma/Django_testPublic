from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login', views.login, name='login'),
    path('sign-up', views.signup, name='signup'),
]
