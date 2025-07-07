from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request, 'movies/index.html')


def detail(request):
    return render(request, 'movies/detail.html')


def search(request):
    return render(request, 'movies/search.html')