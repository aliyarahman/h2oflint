from django.shortcuts import render
from geopy.distance import vincenty
from geopy.geocoders import GoogleV3
from app.models import *
from app.forms import AddDeliveryDateForm, RequestDeliveryForm, IndividualOfferForm, OrganizationForm, DistributionEventForm
import calendar
from datetime import date

def index(request):
    weekday = calendar.day_name[date.today().weekday()]
    if weekday=='Monday':
        locations = Organization.objects.exclude(monday_dist_start='')
    if weekday=='Tuesday':
        locations = Organization.objects.exclude(tuesday_dist_start='')
    if weekday=='Wednesday':
        locations = Organization.objects.exclude(wednesday_dist_start='')
    if weekday=='Thursday':
        locations = Organization.objects.exclude(thursday_dist_start='')
    if weekday=='Friday':
        locations = Organization.objects.exclude(friday_dist_start='')
    if weekday=='Saturday':
        locations = Organization.objects.exclude(saturday_dist_start='')
    if weekday=='Sunday':
        locs = Organization.objects.exclude(sunday_dist_start='')
    return render(request, "index.html", {'locations' : locations})


def request_delivery(request):
    form = RequestDeliveryForm()
    return render(request, "request_delivery.html", {'form' : form})


def organization_offer(request):
    form = IndividualOfferForm()
    return render(request, "organization_offer.html", {'form' : form})


def individual_offer(request):
    form = OrganizationForm()
    return render(request, "individual_offer.html", {'form' : form})

def search(request):
    locations = Organization.objects.all()
    return render(request, "search.html", {'locations' : locations})

def about(request):
    return render(request, "about.html")

def data(request):
    return render(request, "data.html")


def faq(request):
    return render(request, "faq.html")