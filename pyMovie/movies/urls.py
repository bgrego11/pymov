from django.urls import path

from . import views

app_name = "movies" 

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('mov-rando/', views.mov_rando, name='mov-rando'),
    path('show-rando/', views.show_rando, name='show-rando'),
    path('add/', views.add, name='add'),
    path('watch/<int:movie_id>/', views.watched, name='watched'),
    path('search/', views.search, name='search'),
    path('watching/<int:movie_id>/', views.watching, name='watching'),
    path('currently-watching/', views.we_watching, name='we_watching'),
]

