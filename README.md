# assignment
starwars api in Django
1. MUST load planets and movies from the JSON API provided by https://sw-api-rwjfuiltyq-el.a.run.app/
2. MUST expose list APIs - one for movies and one for planets
3. MUST expose APIs to add a movie and planet as a favorite
4. The favorite API should also allow setting a custom title/name to the movie/planet
5. The favorites must be stored per user (user_id can simply be passed in the request, there is no need for authentication)
6. The planet list API must return the name, created, updated, URL, and is_favourite fields
7. The movies list API must return the title, release_date, created, updated, URL, and is_favourite fields
8. If the custom name is set by the user then that should be returned as the name/title and it should be used when searching
9. Additionally, the list APIs must support searching by title/name
