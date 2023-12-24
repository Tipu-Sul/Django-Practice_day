from django.db import models
from musician.models import Musician
import datetime

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    musician=models.ForeignKey(Musician,on_delete=models.CASCADE)
    album_relese_date = models.DateField()

    rating_choices = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    )
    rating = models.CharField(max_length=100, choices=rating_choices)
    
    def __str__(self):
        return self.album_name