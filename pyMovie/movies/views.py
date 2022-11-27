from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse
import random


from django.template import loader

from .models import Movie, MovieForm


def index(request):
    latest_movie_list = Movie.objects.filter(type="Movie")
    shows = Movie.objects.filter(type="Show")
    context = {
        'latest_movie_list': latest_movie_list,
        'shows': shows
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

def add(request):
	print("add call")
	if request.method == "POST":
		movie_form = MovieForm(request.POST)
		if movie_form.is_valid():
			movie_form.save()
			messages.success(request, ('Your movie was successfully added!'))
		else:
			messages.error(request, 'Error saving form')
		
		
		return redirect("movies:index")
	movie_form = MovieForm()
	movies = Movie.objects.all()
	return render(request=request, template_name="movies/add.html", context={'movie_form':movie_form, 'movies':movies})

def watched(request, movie_id):
	movie = get_object_or_404(Movie, pk=movie_id)
	movie.watched=True
	movie.save()
	return render(request, 'movies/detail.html', {'movie': movie})