from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base-view'),
    path('app/home/', views.view_favourites, name='favourite-list'),
    path('app/search/', views.search_planet, name='search-planet'),
    path('app/login/', views.login, name='user-login'),
]