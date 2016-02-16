from django.shortcuts import render
from geopy.distance import vincenty
from geopy.geocoders import GoogleV3
from app.models import WaterDistributionLocation


def index(request):
    locations = WaterDistributionLocation.objects.all()
    return render(request, "index.html", {'locations' : locations})


def request_delivery(request):
    return render(request, "need_delivery.html")


def organization_offer(request):
    return render(request, "we_will_distribute.html")


def individual_offer(request):
    return render(request, "want_to_volunteer.html")


def index_old(request):
    locations = WaterDistributionLocation.objects.all()
    return render(request, "index_old.html", {'locations' : locations})