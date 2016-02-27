from django.shortcuts import render
from django.db.models import Avg

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
    else:
        #Rating.objects.all().aggregate(Avg(rating))
        pass
    return render(request, 'index.html', {"movies": results})


def top_twty(request):
    return render(request, 'top_twenty.html', {})


def movie_view(request, captured_id):
    selected_movie = Movie.objects.get(id=captured_id)
    rating_base = Rating.objects.filter(movie_id=captured_id)
    rating_count = len(list(rating_base))
    rating_avg = round(rating_base.aggregate(Avg('rating')).get('rating__avg'), 2)

    return render(request, 'movie_view.html', {"movie": selected_movie,
                                               "ratings": rating_base,
                                               "avg_ratings": rating_avg,
                                               "count": rating_count}
                  )


def user_view(request):
    return render('user_view.html', {})
