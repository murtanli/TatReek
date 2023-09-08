from django.urls import path
from .views import *

urlpatterns = [
    path('', sign_up.as_view()),
    path('login/', login.as_view())
]