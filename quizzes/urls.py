from django.urls import path
from . import views


urlpatterns = [
    path('2', views.quiz_2, name='quiz2'),
]
