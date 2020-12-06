import json
from django.shortcuts import render
from tiliter_front_end_challenge.services import *


def listings(request):
    add_data_from_json_files()
    context = dict()
    context["theaters"] = Theater.objects.all()

    return render(request, "listings.html", context)
