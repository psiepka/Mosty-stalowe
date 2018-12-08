from django.urls import path
from . import views


urlpatterns = [
    path('test/2', views.quiz_2, name='quiz2'),
    path('<int:lecture>', views.quiz_base, name='quiz_base'),
    path('start/<int:lecture>/', views.quiz_start, name='quiz_start'),
]
