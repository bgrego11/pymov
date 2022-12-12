from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save


now = datetime.now()

# Create your models here.
class Movie(models.Model):
   
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=[('Movie',"Movie"),('Show','Show')])
    body = models.CharField(max_length=200, null=True)
    watched = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    currently_watching = models.BooleanField(default=False)
    trailer = models.CharField(max_length=200, null=True, blank=True)
    xmas = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title
    
@receiver(pre_save, sender=Movie)
def Movie_save_handler(sender, instance, *args, **kwargs):
    if instance.trailer:
        sep = "&ab_channel"
        instance.trailer = instance.trailer.replace("watch?v=","embed/").split(sep,1)[0]
     

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title','type','body','watched', 'currently_watching', 'trailer','xmas']