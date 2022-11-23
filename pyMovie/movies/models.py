from django.db import models

# Create your models here.
class Movie(models.Model):
   
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=[('Movie',"Movie"),('Show','Show')])
    body = models.CharField(max_length=200, null=True)
    watched = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')