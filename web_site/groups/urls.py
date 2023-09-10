from django.urls import path

from .views import *

urlpatterns = [
    path('', addgroups, name='addgroup'),
    path('choice_game/', choice_game.as_view(), name = 'choice_game')
]