from django.contrib import admin
from .models import Movie, Theatre, Show, Seats

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'poster', 'release_date', 'duration', 'genre')

class TheatreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

class ShowAdmin(admin.ModelAdmin):
    list_display = ('movie', 'theatre', 'start_time', 'end_time', 'price')   

class SeatsAdmin(admin.ModelAdmin):
    list_display = ('show', 'seat_number', 'is_available')
   

admin.site.register(Movie, MovieAdmin)
admin.site.register(Theatre, TheatreAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Seats, SeatsAdmin )



