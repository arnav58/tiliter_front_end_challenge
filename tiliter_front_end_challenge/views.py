import json
from django.shortcuts import render
from tiliter_front_end_challenge.services import *


def listings(request):
    load_data_from_json_files(force_update=False)
    context = dict()
    context["theaters"] = Theater.objects.all()

    return render(request, "listings.html", context)
