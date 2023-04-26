from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
import requests

from .models import Movie

def format(data):
    """ ToDo:
        - Create common helper functions to be used across modules (movies & planets)
    """
    existing_movie_swapi_ids = list(Movie.objects.values_list('swapi_id', flat=True))
    existing_movie_favourites = list(Movie.objects.values_list('is_favourite', flat=True))
    movies = data['results']
    formatted_movies = []
    for movie in movies:
        movie_url = movie['url']
        swapi_id = int(movie_url.split("api/films/",1)[1].split('/',1)[0])
        try:
            existing_movie_index = existing_movie_swapi_ids.index(swapi_id)
            is_favourite = existing_movie_favourites[existing_movie_index]
        except ValueError:
            is_favourite = False
        formatted_movie = {
            'swapi_id': swapi_id,
            'title': movie['title'],
            'is_favourite': is_favourite,
            'release_date': movie['release_date'],
            'created': movie['created'],
            'updated': movie['edited'],
            'url': movie['url']
        }
        formatted_movies.append(formatted_movie)

    return formatted_movies


def list_movies(request):
    response = requests.get('https://swapi.dev/api/films/')
    data = response.json()
    formatted_movies = format(data)
    return render(request, 'movies/list.html', {'movies': formatted_movies})


def update_favourite(request, swapi_id, movie_title):
    swapi_int = int(swapi_id)
    try:
        movie = Movie.objects.get(swapi_id=swapi_int)
        movie.is_favourite = not movie.is_favourite 
        movie.save()
    except Movie.DoesNotExist:
        Movie.objects.create(swapi_id=swapi_int, title=movie_title, is_favourite=True)

    return HttpResponseRedirect('/app/home')

def update_favourite_movie(request, swapi_id, movie_title):
    
    if request.method == 'POST':
        
        new_movie_title = request.POST.get('movie_title')

        
        url = f'https://swapi.dev/api/films/{swapi_id}/'
        headers = {'content-type': 'application/json'}

        data = {'title': new_movie_title}
        response = requests.patch(url, headers=headers, json=data)

        if response.status_code == 200:
            favourite_movie = Movie.objects.get(user=request.user, swapi_id=swapi_id)
            favourite_movie.title = new_movie_title
            favourite_movie.save()

            return redirect('update')
        else:
            error_message = 'Failed to update the movie. Please try again later.'
            context = {'error_message': error_message}
            return render(request, 'update_favourite_movie.html', context)
    else:
        context = {'movie_title': movie_title}
        return render(request, 'update_favourite_movie.html', context)
