from django.db import models


class Movie(models.Model):
    movie_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    rating = models.CharField(max_length=10)
    poster_url = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Theater(models.Model):
    theater_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_all_movies_listed(self):
        return TheaterMovieListing.objects.filter(theater=self)


class TheaterMovieListing(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.theater.name} showing {self.movie.title}"


class MovieShowtime(models.Model):
    movie_listing = models.ForeignKey(TheaterMovieListing, on_delete=models.CASCADE)
    showtime = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.movie_listing} at {self.showtime}"
