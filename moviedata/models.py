from django.db import models


# Create your models here.
class moviedata(models.Model):
    ACTION = 'ACTION'
    COMEDY = 'COMEDY'
    HORROR = 'HORROR'
    ADVENTURE = 'ADVENTURE'
    CRIME = 'CRIME'
    DRAMA = 'DRAMA'

    MOVIE_TYPES = [
        (ACTION, 'ACTION'),
        (COMEDY, 'COMEDY'),
        (HORROR, 'HORROR'),
        (ADVENTURE, 'ADVENTURE'),
        (DRAMA, 'DRAMA'),
        (CRIME, 'CRIME'),

    ]
    name = models.CharField(max_length=255, unique=True, blank=False)
    ratings = models.DecimalField(max_digits=2, decimal_places=1)
    runtime = models.DecimalField(max_digits=2, decimal_places=1,default=1.0)
    movie_type = models.CharField(max_length=255, choices=MOVIE_TYPES, default='ACTION')
    review=models.TextField(max_length=1000,blank=True)
    image=models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.name
