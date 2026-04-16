from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('username/<str:material>/', views.username, name='username'),
    path('quiz/<str:material>/', views.quiz, name='quiz'),
    path('result/', views.result, name='result'),
    path('history/', views.history, name='history'),
]