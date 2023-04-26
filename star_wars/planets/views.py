from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests

from .models import Planet

def format(data):
    """ Get the swapi_ids of existing favourite planets
        - When iterating through planets fetched from swapi, 
            - mark them as favourite & pass to frontend.
        - When marking planet as favourite/un-favourite, 
            - update same in DB by passing swapi_id
        ToDo:
            - Create common helper functions to be used across modules
    """
    existing_planet_swapi_ids = list(Planet.objects.values_list('swapi_id', flat=True))
    existing_planet_favourites = list(Planet.objects.values_list('is_favourite', flat=True)) # Todo: Did this for quick mapping, change it to remove favourites
    
    planets = data['results']
    formatted_planets = []
    for planet in planets:
        planet_url = planet['url']
        swapi_id = int(planet_url.split("api/planets/",1)[1].split('/',1)[0])
        try:
            existing_planet_index = existing_planet_swapi_ids.index(swapi_id)
            is_favourite = existing_planet_favourites[existing_planet_index]
        except ValueError:
            is_favourite = False
        formatted_planet = {
            'swapi_id': swapi_id,
            'name': planet['name'],
            'is_favourite': is_favourite,
            'created': planet['created'],
            'updated': planet['edited'],
            'url': planet['url']
        }
        formatted_planets.append(formatted_planet)

    return formatted_planets


def list_planets(request, page_number=1):
    endpoint = 'https://swapi.dev/api/planets/?page='
    url = endpoint + str(page_number)
    response = requests.get(url)
    data = response.json()
    formatted_planets = format(data)
    return render(request, 'planets/list.html', {'planets': formatted_planets})


def update_favourite(request, swapi_id, planet_name):
    """
        1. If Swapi_id is present, update is_favourite to !is_favourite
        2. If swapi_id is not present,
            - Create a new record in Planet & set favourite to True
    """
    swapi_int = int(swapi_id)
    try:
        planet = Planet.objects.get(swapi_id=swapi_int)
        planet.is_favourite = not planet.is_favourite 
        planet.save()
    except Planet.DoesNotExist:
        
        Planet.objects.create(swapi_id=swapi_int, name=planet_name, is_favourite=True)

    return HttpResponseRedirect('/app/home')
