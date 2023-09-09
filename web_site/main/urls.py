from django.urls import path
from .views import *
urlpatterns = [
    path('', main,name = 'home'),
    path('choice_game/', choice_game, name = 'choice_game')
]