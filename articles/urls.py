from django.urls import path
from . import views

urlpatterns = [
    path('1', views.wyklad_1, name='wyklad1'),
    path('2', views.wyklad_2, name='wyklad2'),
    path('3', views.wyklad_3, name='wyklad3'),
    path('4', views.wyklad_4, name='wyklad4'),
    path('5', views.wyklad_5, name='wyklad5'),
    path('6', views.wyklad_6, name='wyklad6'),
    path('7', views.wyklad_7, name='wyklad7'),
    path('8', views.wyklad_8, name='wyklad8'),
    path('9', views.wyklad_9, name='wyklad9'),
]