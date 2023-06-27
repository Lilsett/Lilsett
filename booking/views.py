from django.shortcuts import render
from django.http import request
from django.views.generic import ListView, DetailView
from .models import Movie, Theatre, Show
from django.contrib.auth.decorators import login_required
from .models import Movie

def index(request):
    movie_list = Movie.objects.all()
    theatre_list = Theatre.objects.all()
    show_list = Show.objects.all()

    context = {
        'movie_list': movie_list,
        'theatre_list': theatre_list,
        'show_list': show_list,
    }
    return render(request, 'booking/index.html', context)

class MovieListView(ListView):
    model = Movie
    template_name = 'booking/movie_list.html'
    context_object_name = 'movie_list'
class MovieDetailView(DetailView):
    model = Movie
    template_name = 'booking/movie_detail.html'
    context_object_name = 'movie'   

class TheatreListView(ListView):
    model = Theatre
    template_name = 'booking/theatre_list.html'
    context_object_name = 'theatre_list'    

class TheatreDetailView(DetailView):
    model = Theatre
    template_name = 'booking/theatre_detail.html'
    context_object_name = 'theatre'     

class ShowListView(ListView):
    model = Show
    template_name = 'booking/show_list.html'
    context_object_name = 'show_list' 

class ShowDetailView(DetailView):
    model = Show
    template_name = 'booking/show_detail.html'
    context_object_name = 'show'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        show = self.object
        seats = show.seats_set.all()
        context['seats'] = seats
        return context   

def movie_list(request):
    movie_list = Movie.objects.all()  
    context = {'movie_list': movie_list}
    return render(request, 'movie_list.html', context)

