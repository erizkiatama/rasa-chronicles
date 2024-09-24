from django.contrib import admin

from .models import Book, Genre, BookVolume, Movie, Game, GamePlatform

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(BookVolume)
admin.site.register(Movie)
admin.site.register(Game)
admin.site.register(GamePlatform)
