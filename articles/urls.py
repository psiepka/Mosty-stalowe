from django.urls import path
from . import views

urlpatterns = [
    path('1', views.wyklad_1, name='wyklad1'),
    path('2', views.wyklad_2, name='wyklad2'),
    path('3', views.wyklad_3, name='wyklad3'),
    path('4', views.wyklad_4, name='wyklad4'),
    path('5', views.wyklad_5, name='wyklad5'),
]