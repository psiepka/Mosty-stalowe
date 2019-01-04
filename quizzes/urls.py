from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('lista/', TemplateView.as_view(template_name="quizzes/quiz_list.html"), name='quiz_list'),
    path('<int:lecture>/', views.quiz_start, name='quiz_start'),
    path('<int:lecture>/start/', views.quiz_start, name='quiz_start'),
    path('<int:lecture>/<int:question>/', views.quiz_base, name='quiz_base'),
    path('<int:lecture>/result/', views.quiz_result, name='quiz_result'),
    path('mega/', views.quiz_mega_start, name='quiz_mega_start'),
    path('mega/<int:question>/', views.quiz_mega, name='quiz_mega'),
    path('all/<int:lecture>/', views.quiz_view_all, name='quiz_view_all'),
]
