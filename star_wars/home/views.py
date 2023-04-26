from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
import requests

from planets.models import Planet
from movies.models import Movie

def base(request):
    return HttpResponseRedirect('/app/login')

def login(request):
    return render(request, 'base/login.html')


def view_favourites(request):
    favourite_movies = Movie.objects.filter(is_favourite=True)
    favourite_planets = Planet.objects.filter(is_favourite=True)

    return render(request, 'home/favourites.html', 
                    {'favourite_movies': favourite_movies, 'favourite_planets': favourite_planets})


def format(planet):
    planet_url = planet['url']
    swapi_id = int(planet_url.split("api/planets/",1)[1].split('/',1)[0])
    planet['swapi_id'] = swapi_id
    try:
        existing_planet = Planet.objects.get(swapi_id=swapi_id)
        planet['is_favourite'] = existing_planet.is_favourite
    except ObjectDoesNotExist:
        planet['is_favourite'] = False
    return planet

def search_planet(request):
    if request.method == 'POST':
        planet_name = request.POST.get('planet_name')
        if planet_name:
            endpoint = 'https://swapi.dev/api/planets/?search=' 
            url = endpoint + planet_name
            response = requests.get(url)
            data = response.json()
            if data['count'] is not 0:
                planet = data['results'][0]
                formatted_planet = format(planet)
                return render(request, 'home/search_result.html', {'planet': formatted_planet})

    # If search result not found or not a POST request
    return HttpResponseRedirect('/app/home')
