from django.urls import path
from .views import *
urlpatterns = [
    path('', main.as_view(),name = 'home'),
]