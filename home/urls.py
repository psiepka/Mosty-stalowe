from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kontakt/', views.contact, name='contact'),
    path('biblografia/', views.biblography, name='bibliography'),
]