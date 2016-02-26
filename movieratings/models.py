from django.db import models

# Create your models here.

GENDER_CHOICES = [
    ('F', 'Female'),
    ('M', 'Male')
]


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=30)
    video_release_date = models.CharField(max_length=30, blank=True)
    imdb_url = models.URLField()
    unknown_genre = models.BooleanField(default=0)
    action = models.BooleanField(default=0)
    adventure = models.BooleanField(default=0)
    animation = models.BooleanField(default=0)
    childrens = models.BooleanField(default=0)
    comedy = models.BooleanField(default=0)
    crime = models.BooleanField(default=0)
    documentary = models.BooleanField(default=0)
    drama = models.BooleanField(default=0)
    fantasy = models.BooleanField(default=0)
    film_noir = models.BooleanField(default=0)
    horror = models.BooleanField(default=0)
    musical = models.BooleanField(default=0)
    mystery = models.BooleanField(default=0)
    romance = models.BooleanField(default=0)
    sci_fi = models.BooleanField(default=0)
    thriller = models.BooleanField(default=0)
    war = models.BooleanField(default=0)
    western = models.BooleanField(default=0)

    def __str__(self):
        return self.title

class User(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    zip_code = models.CharField(max_length=10)



class Rating(models.Model):
    user = models.ForeignKey(User)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()

    def __str__(self):
        return "{} Stars".format(self.rating)