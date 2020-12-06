import json

from django.http import JsonResponse
from django.shortcuts import render
from tiliter_front_end_challenge.services import *
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt


def listings(request):
    load_data_from_json_files(force_update=False)
    context = dict()
    theaters = Theater.objects.all()
    context["theaters"] = theaters
    context["movie_listing_details_raw"] = "\n".join([render_to_string("movie-listing.html", {"movie_listing": movie_listing}) for movie_listing in theaters.first().get_all_movies_listed()])

    return render(request, "listings.html", context)


@csrf_exempt
def get_listings(request):
    context = dict()
    theater_id = int(request.POST.get('theater_id', 1))
    theater = Theater.objects.get(pk=theater_id)

    search_term = request.POST.get('search_term', None)
    if search_term is not None:
        filtered_movie_listings = theater.get_filtered_movie_listed(search_term)
    else:
        filtered_movie_listings = theater.get_all_movies_listed()

    context["movie_listing_details_raw"] = "\n".join([render_to_string("movie-listing.html", {"movie_listing": movie_listing}) for movie_listing in filtered_movie_listings])

    return JsonResponse(context)