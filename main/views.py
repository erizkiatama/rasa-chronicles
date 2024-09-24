from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import User


def index(request):
    return render(request, 'home.html', {'users': User.objects.all()})


def about_us(request):
    return render(request, 'about_us.html', {'users': User.objects.all()})


def under_construction(request):
    return render(request, 'under_construction.html', status=HttpResponseNotFound.status_code)
