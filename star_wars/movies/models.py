from django.db import models

class Movie(models.Model):
    swapi_id = models.IntegerField()
    title = models.CharField(max_length=150)

    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return f'title: {self.title}, swapi_id:{self.swapi_id}, is_favourite:{self.is_favourite}'
