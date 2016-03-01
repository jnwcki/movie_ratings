from django.shortcuts import render
from django.db.models import Avg, Count

# Create your views here.
from movieratings.models import Movie, Rating, User


def make_index(request, *args):
    m_search = request.POST.get('movie_search')
    results = []
    if m_search:
        results = Movie.objects.filter(title__contains=m_search)
    return render(request, 'index.html', {"movies": results})


def top_twty(request):
    review_twty = Movie.objects.annotate(average_rating=Avg('rating__rating')).values('pk', 'title', 'average_rating').order_by('-average_rating')[:20]

    return render(request, 'top_twenty.html', {"top_twty": review_twty})


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


def user_view(request, captured_id):
    rater_id = captured_id
    rater_base = User.objects.get(id=rater_id)
    all_ratings = Rating.objects.filter(user=rater_id)

    return render(request, 'user_view.html', {'rater_id': rater_id,
                                              'rater_info': rater_base,
                                              'all_ratings': all_ratings,
                                              }
                  )
