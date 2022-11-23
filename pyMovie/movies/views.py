from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
import random


from django.template import loader

from .models import Movie


def index(request):
    latest_movie_list = Movie.objects.order_by('-pub_date')
    context = {
        'latest_movie_list': latest_movie_list,
    }
    return render(request, 'movies/index.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})

def rando(request):
    latest_movie_list = Movie.objects.filter(watched=False)
    movie = random.choice(latest_movie_list)
    print(latest_movie_list)
    print(movie)
    return render(request,'movies/rando.html',{'movie': movie})
