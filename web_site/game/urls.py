from django.urls import path, re_path
from .views import *
urlpatterns = [
    re_path(r'^[a-zA-Z0-9]+/$', game,name='game'),
    path('finish/', stop, name='stop')
]