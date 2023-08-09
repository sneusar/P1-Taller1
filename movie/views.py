from django.shortcuts import render

from .models import Movie

# Create your views here.


def home(request):

    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html', {'searchTerm': searchTerm})


def about(request):
    return render(request, 'about.html')

