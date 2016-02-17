from django.shortcuts import render
from geopy.distance import vincenty
from geopy.geocoders import GoogleV3
from app.models import WaterDistributionLocation
from app.forms import RequestDeliveryForm, IndividualOfferForm, OrganizationForm, DistributionEventForm

def index(request):
    locations = WaterDistributionLocation.objects.all()
    return render(request, "index.html", {'locations' : locations})


def request_delivery(request):
    form = RequestDeliveryForm()
    return render(request, "request_delivery.html", {'form' : form})


def organization_offer(request):
    form = IndividualOfferForm()
    return render(request, "organization_offer.html", {'form' : form})


def individual_offer(request):
    form = OrganizationOfferForm()
    return render(request, "individual_offer.html", {'form' : form})


def index_old(request):
    locations = WaterDistributionLocation.objects.all()
    return render(request, "index_old.html", {'locations' : locations})