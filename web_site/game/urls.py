from django.urls import path
from .views import *
urlpatterns = [
    path('<str:room_name>/', game,name='game'),
    path('finish/', stop, name='stop')
]