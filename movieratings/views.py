import json

from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Avg, Count

# Create your views here.
from django.views.generic import View

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
    try:
        rating_avg = round(rating_base.aggregate(Avg('rating')).get('rating__avg'), 2)
    except TypeError:
        rating_avg = 0
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


class MovieListApiView(View):
    def get(self, request):
        data = list(Movie.objects.all().values())
        return HttpResponse(json.dumps(data), content_type="application/json")

    def post(self, request):
        title = request.POST['title'],
        release_date = request.POST['release_date']
        video_release_date = request.POST['video_release_date']
        imdb_url = request.POST['imdb_url']
        unknown_genre = request.POST['unknown_genre']
        action = request.POST['action']
        adventure = request.POST['adventure']
        animation = request.POST['animation']
        childrens = request.POST['childrens']
        comedy = request.POST['comedy']
        crime = request.POST['crime']
        documentary = request.POST['documentary']
        drama = request.POST['drama']
        fantasy = request.POST['fantasy']
        film_noir = request.POST['film_noir']
        horror = request.POST['horror']
        musical = request.POST['musical']
        mystery = request.POST['mystery']
        romance = request.POST['romance']
        sci_fi = request.POST['sci_fi']
        thriller = request.POST['thriller']
        war = request.POST['war']
        western = request.POST['western']

        model_to_dict(Movie.objects.create(title=title, release_date=release_date,
                             video_release_date=video_release_date,
                             imdb_url=imdb_url, unknown_genre=unknown_genre,
                             action=action, adventure=adventure, animation=animation,
                             childrens=childrens, comedy=comedy, crime=crime,
                             documentary=documentary, drama=drama, fantasy=fantasy,
                             film_noir=film_noir, horror=horror, musical=musical,
                             mystery=mystery, romance=romance, sci_fi=sci_fi,
                             thriller=thriller, war=war, western=western))

        return HttpResponse(content_type='application/json', status=201)


class RatingListApiView(View):
    def get(self, request):
        data = list(Rating.objects.all().values())
        return HttpResponse(json.dumps(data), content_type="application/json")


class UserListApiView(View):
    def get(self, request):
        data = list(User.objects.all().values())
        return HttpResponse(json.dumps(data), content_type="application/json")


class MovieDetailApiView(View):
    def get(self, request, pk):
        data = model_to_dict(Movie.objects.get(pk=pk))
        return HttpResponse(json.dumps(data), content_type="application/json")


class RatingDetailApiView(View):
    def get(self, request, pk):
        data = model_to_dict(Rating.objects.get(pk=pk))
        return HttpResponse(json.dumps(data), content_type="application/json")


class UserDetailApiView(View):
    def get(self, request, pk):
        data = model_to_dict(User.objects.get(pk=pk))
        return HttpResponse(json.dumps(data), content_type="application/json")

