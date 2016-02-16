from django.shortcuts import render
from geopy.distance import vincenty
from geopy.geocoders import GoogleV3
from app.models import WaterDistributionLocation


def index(request):
    locations = WaterDistributionLocation.objects.all()
    return render(request, "index.html", {'locations' : locations})

def option2(request):
    locations = WaterDistributionLocation.objects.all()
    return render(request, "option2.html", {'locations' : locations})

def north(request):
    return render(request, "north.html")

def need_delivery(request):
    return render(request, "need_delivery.html")

def i_donated(request):
    return render(request, "i_donated.html")

def received_water(request):
    return render(request, "received_water.html")

def service(request):
    return render(request, "service.html")

def want_to_donate(request):
    return render(request, "want_to_donate.html")

def want_to_volunteer(request):
    return render(request, "want_to_volunteer.html")

def we_will_distribute(request):
    return render(request, "we_will_distribute.html")
