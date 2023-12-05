from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomeView, name="home"),
    path("search/", views.SearchView, name="search") #New
]
