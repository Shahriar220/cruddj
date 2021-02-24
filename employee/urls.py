from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('employee/',include('register.urls')),
    path('admin/', admin.site.urls),
]
