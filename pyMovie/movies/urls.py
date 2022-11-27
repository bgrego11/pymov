from django.urls import path

from . import views

app_name = "movies" 

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('rando/', views.rando, name='rando'),
    path('add/', views.add, name='add'),
    path('watch/<int:movie_id>/', views.watched, name='watched'),

]