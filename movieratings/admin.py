from django.contrib import admin
from movieratings.models import Movie, Rating, User
# Register your models here.
admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Rating)

