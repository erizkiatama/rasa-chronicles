from django.db import models

from main.models import User


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image_url = models.ImageField(upload_to='collection/static/images/books/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    genres = models.ManyToManyField('Genre')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'genres'

    def __str__(self):
        return self.name


class BookVolume(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='volumes')
    volume_number = models.IntegerField()
    cover_image_url = models.ImageField(upload_to='collection/static/images/bookvolumes/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'book_volumes'
        indexes = [
            models.Index(fields=['book']),
        ]

    def __str__(self):
        return f"{self.book.title} - Volume {self.volume_number}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    synopsis = models.TextField(null=True, blank=True)
    image_url = models.ImageField(upload_to='collection/static/images/movies/')
    release_year = models.IntegerField()
    director = models.CharField(max_length=255)
    esrb_rating = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    genres = models.ManyToManyField('Genre')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'movies'

    def __str__(self):
        return self.title


class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image_url = models.ImageField(upload_to='collection/static/images/games/')
    release_date = models.DateField()
    developer = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    esrb_rating = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    genres = models.ManyToManyField('Genre')
    platforms = models.ManyToManyField('GamePlatform')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'games'

    def __str__(self):
        return self.title


class GamePlatform(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'game_platforms'

    def __str__(self):
        return self.name
