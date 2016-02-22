from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.core.mail import send_mass_mail
from django.forms.models import model_to_dict
from django.conf import settings
from geopy.distance import vincenty
from geopy.geocoders import GoogleV3
from app.models import *
from app.forms import CustomLoginForm, AddDeliveryDateForm, RequestDeliveryForm, IndividualOfferForm, OrganizationForm, DistributionEventForm, EditIndividualForm, EditOrganizationForm, AddAnotherHelpOfferForm
import calendar
from datetime import date

def locations(request):
    return render(requestion, 'placeholder.html')