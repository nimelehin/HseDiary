from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reply_to_alice/', views.reply_to_alice, name='reply to alice'),
    path('reply_to_ga/', views.reply_to_ga, name='reply to GA'),
]
