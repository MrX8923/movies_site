from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'movies_genre'


class Actor(models.Model):
    firstname = models.CharField(max_length=30, null=True, blank=True)
    lastname = models.CharField(max_length=30, null=True, blank=True)
    birthday = models.DateField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    portrait = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    class Meta:
        db_table = 'movies_actor'


class Country(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'movies_country'


class Director(models.Model):
    firstname = models.CharField(max_length=30, null=True, blank=True)
    lastname = models.CharField(max_length=30, null=True, blank=True)
    portrait = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    class Meta:
        db_table = 'movies_director'


class AgeRating(models.Model):
    choices = (('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17'))
    rate = models.CharField(max_length=30, choices=choices, null=True, blank=True)

    def __str__(self):
        return self.rate

    class Meta:
        db_table = 'movies_age_rating'


class Subscription(models.Model):
    choices = (('бесплатно', 'бесплатно'), ('базовая', 'базовая'), ('СУПЕР', 'СУПЕР'))
    name = models.CharField(max_length=30, choices=choices, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'movies_subscription'


class Movie(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название', null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_DEFAULT, default=1, null=True, blank=True)
    rating = models.FloatField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=500, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    age_rating = models.ForeignKey(AgeRating, on_delete=models.SET_DEFAULT, default=1, null=True, blank=True)
    actors = models.ManyToManyField(Actor)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_DEFAULT, default=1, null=True, blank=True)
    poster = models.CharField(max_length=100, null=True, blank=True, verbose_name='Постер')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'movies_table'

    def display_actors(self):
        return ', '.join([actor.firstname + ' ' + actor.lastname for actor in self.actors.all()])
    display_actors.short_description = 'Актеры'

    def get_absolute_url(self):
        return reverse('info', args=[self.id, self.title])


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.SET_NULL, null=True)
    comment_text = models.TextField(max_length=500, null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.date_published} by {self.author.username} for {self.movie.title}'

    class Meta:
        db_table = 'comments'
        ordering = ('date_published',)


models_tuple = (Genre, Country, AgeRating, Subscription, Comments)
