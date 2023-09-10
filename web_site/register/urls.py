from django.urls import path
from .views import *

urlpatterns = [
    path('', sign_up.as_view(), name = 'signup'),
    path('login/', login.as_view(), name = 'login'),
    path('logout/', logout_user, name = 'logout')
]