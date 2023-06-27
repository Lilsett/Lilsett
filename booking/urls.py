from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.index, name='index.'),
    path('movies/', views.MovieListView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('theatres/', views.TheatreListView.as_view(), name='theatre_list'),
    path('theatres/<int:pk>/', views.TheatreDetailView.as_view(), name='theatre_detail'),
    path('shows/', views.ShowListView.as_view(), name='show_list'),
    path('shows/<int:pk>/', views.ShowDetailView.as_view(), name='show_detail'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
] + static('/movies/', document_root=settings.MEDIA_ROOT)
