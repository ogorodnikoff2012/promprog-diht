from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('questions', views.QuestionList.as_view(), name='questions'),
    path('questions/new', views.new_question, name='new_question'),
    url(r'^questions/answer/([0-9]+)$', views.new_answer, name='new_answer')
]
