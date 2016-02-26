from django.shortcuts import render


# Create your views here.
from movieratings.models import Movie, Rating


def make_index(request):
    m_search = request.POST.get('movie_search')
    results = ''
    print("inside make_index", m_search)
    if m_search:
        results = Movie.objects.filter(title__contains=m_search)
        print("inside m_search function", request.POST.get('movie_search'))
        print(results)
    return render(request, 'index.html', {"movies": results})


def top_twty(request):
    return render(request, 'top_twenty.html', {})


def movie_view(request, captured_id):
    selected_movie = Movie.objects.get(id=captured_id)
    rating_base = Rating.objects.filter(movie_id=captured_id)

    return render(request, 'movie_view.html', {"movie": selected_movie, "ratings": rating_base})


def user_view(request):
    return render('user_view.html', {})
