from django.urls import path
from django.conf.urls import url
from . import views
from .models import Question

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:question_label>', views.question_page, name='question'),
]

