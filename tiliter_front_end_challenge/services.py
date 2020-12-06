from tiliter_front_end_challenge.models import *
import json


def add_data_from_json_files():

    if Movie.objects.exists():
        return

    movie_meta_f = open('data/movie_metadata.json').read()
    movie_metadata = json.loads(movie_meta_f)

    for movie in movie_metadata:
        new_movie = Movie(movie_id=movie["id"], title=movie["title"], rating=movie["rating"], poster_url=movie["poster"])
        new_movie.save()

    theater_showtimes_f = open('data/theater_showtimes.json').read()
    theater_showtimes_data = json.loads(theater_showtimes_f)

    for theater_details in theater_showtimes_data:
        theater = Theater(theater_id=theater_details["id"], name=theater_details["name"])
        theater.save()

        theater_showtimes = theater_details["showtimes"]
        movies_listed = list(theater_showtimes.keys())

        for movie_id in movies_listed:
            movie = Movie.objects.filter(movie_id=movie_id).first()
            theater_movie_listing = TheaterMovieListing(theater=theater, movie=movie)
            theater_movie_listing.save()

            for showtime in theater_showtimes[movie_id]:
                movie_showtime = MovieShowtime(movie_listing=theater_movie_listing, showtime=showtime)
                movie_showtime.save()
    return
