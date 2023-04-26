from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_movies, name='movie-list'),
    path('update_favourite/<int:swapi_id>/<str:movie_title>/', views.update_favourite, name='update-favourite-movie'),
    #path('update/<int:swapi_id>/<str:movie_title>/',views.update_favourite_movie, name='update-favourite-movie'),
]