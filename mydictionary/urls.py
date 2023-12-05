from django.contrib import admin
from django.urls import path, include # New

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("dictionary.urls")) # New
]