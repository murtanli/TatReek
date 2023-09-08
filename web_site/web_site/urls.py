
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('sign_up/', include('register.urls')),
    path('groups/', include('groups.urls')),
    path('admin/', admin.site.urls),
]
