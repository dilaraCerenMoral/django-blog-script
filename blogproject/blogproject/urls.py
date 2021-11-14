from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('admin/', include('django.contrib.auth.urls')),
    path('', include('blogapp.urls')),
]
