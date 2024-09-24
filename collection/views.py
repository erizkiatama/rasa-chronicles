from django.shortcuts import render

from main.models import User
from .models import Book, Movie, Game
from .forms import CollectionFilterForm


def get_books(owner_ids):
    collections = []

    # Fetch all books with its genres
    books = Book.objects.prefetch_related("genres").all()

    # Filter by owner ids
    if owner_ids is not None and len(owner_ids) > 0:
        books = books.filter(owner__in=owner_ids)

    # Put in the collections context
    for book in books:
        collections.append({"item": book, "type": "book"})

    return collections


def get_movies(owner_ids):
    collections = []

    # Fetch all books with its genres
    movies = Movie.objects.prefetch_related("genres").all()

    # Filter by owner ids
    if owner_ids is not None and len(owner_ids) > 0:
        movies = movies.filter(owner__in=owner_ids)

    # Put in the collections context
    for movie in movies:
        collections.append({"item": movie, "type": "film"})

    return collections


def get_games(owner_ids):
    collections = []

    # Fetch all books with its genres
    games = Game.objects.prefetch_related("genres").all()

    # Filter by owner ids
    if owner_ids is not None and len(owner_ids) > 0:
        games = games.filter(owner__in=owner_ids)

    # Put in the collections context
    for game in games:
        collections.append({"item": game, "type": "gamepad"})

    return collections


def collection(request):
    form = CollectionFilterForm(request.GET)

    # Init filters
    category = None
    owner_ids = None

    # Init queryset
    collections = []

    if form.is_valid():
        category = form.cleaned_data["category"]
        owner_ids = form.cleaned_data["owner"]

    is_get_all_collections = category is None or len(category) == 0

    # Get by categories or get all if categories aren't provided
    if is_get_all_collections or "book" in category:
        collections += get_books(owner_ids)
    if is_get_all_collections or "movie" in category:
        collections += get_movies(owner_ids)
    if is_get_all_collections or "game" in category:
        collections += get_games(owner_ids)

    # sort the collection based on data creation
    collections = sorted(collections, key=lambda c: c["item"].created_at)

    return render(request, "collection.html", {
        "form": form, "users": User.objects.all(), "collections": collections
    })
