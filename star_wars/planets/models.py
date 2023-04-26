from django.db import models

class Planet(models.Model):
    swapi_id = models.IntegerField()
    name = models.CharField(max_length=300)

    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return f'name: {self.name}, swapi_id:{self.swapi_id}, is_favourite:{self.is_favourite}'
