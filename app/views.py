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
from app.forms import CustomLoginForm, AddDeliveryDateForm, RequestDeliveryForm, IndividualOfferForm, OrganizationForm, DistributionEventForm, EditIndividualForm, EditOrganizationForm, AddAnotherHelpOfferForm, EditRequestDeliveryForm, CallTimeForm
import calendar
from datetime import date
from django.core import serializers

def login_view(request):
    form = CustomLoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            if user.is_staff:
                return HttpResponseRedirect(reverse('staff_dashboard'))
            else:
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'login.html', {'form': form })

def logout_view(request):
    logout(request)
    return render(request, 'logged_out.html')


def search(request):
    locations = Organization.objects.all()
    return render(request, "search.html", {'locations' : locations})

def about(request):
    return render(request, "about.html")

def data(request):
    return render(request, "data.html")

def faq(request):
    return render(request, "faq.html")

def changes_updated(request):
    return render(request, "changes_updated.html")

def request_received(request):
    return render(request, "request_received.html")

def register(request):
    return render(request, "register.html")

def privacy(request):
    return render(request, "privacy.html")

def terms(request):
    return render(request, "terms.html")



def index(request):
    weekday = calendar.day_name[date.today().weekday()]
    if weekday=='Monday':
        locations = Organization.objects.exclude(monday_dist_start='')
    elif weekday=='Tuesday':
        locations = Organization.objects.exclude(tuesday_dist_start='')
    elif weekday=='Wednesday':
        locations = Organization.objects.exclude(wednesday_dist_start='')
    elif weekday=='Thursday':
        locations = Organization.objects.exclude(thursday_dist_start='')
    elif weekday=='Friday':
        locations = Organization.objects.exclude(friday_dist_start='')
    elif weekday=='Saturday':
        locations = Organization.objects.exclude(saturday_dist_start='')
    elif weekday=='Sunday':
        locations = Organization.objects.exclude(sunday_dist_start='')
    return render(request, "index.html", {'locations' : locations, 'weekday': weekday})


def staff_dashboard(request):
    helpoffers = IndividualHelpOffer.objects.all()
    organizations = Organization.objects.all()
    delivery_requests = DeliveryRequest.objects.all()
    return render(request, "staff_dashboard.html", {'helpoffers' : helpoffers, 'delivery_requests': delivery_requests})


def call_time_notes(request, offer_id):
    offer = IndividualHelpOffer.objects.get(id=offer_id)
    data = model_to_dict(offer)
    if request.method == "POST":
        form = CallTimeForm(request.POST)
        if form.is_valid():
            offer.resolved = form.cleaned_data.get("resolved")
            offer.left_message = form.cleaned_data.get("left_message")
            offer.action_needed = form.cleaned_data.get("action_needed")
            offer.no_contact = form.cleaned_data.get("no_contact")
            offer.calltime_notes = form.cleaned_data.get("calltime_notes")
            offer.save()
            return HttpResponseRedirect(reverse('staff_dashboard'))
    else:
        form = CallTimeForm(initial=model_to_dict(offer))
    return render(request, "call_time_notes.html", {'offer' : offer, 'form':form, 'data':data})


def request_delivery(request):
    if request.method == "POST":
        form = RequestDeliveryForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("contact_email")
            password = form.cleaned_data.get("password")
            u = User.objects.create_user(email, email, password)
            u.first_name = form.cleaned_data.get("recipient_first")
            u.last_name = form.cleaned_data.get("recipient_last")
            u.save()
            user = authenticate(username=email, password=password)
            login(request, user)
            u = User.objects.filter(email = email).first()

            r = DeliveryRequest(user = u)
            r.reason = form.cleaned_data.get("reason")
            r.recipient_first = form.cleaned_data.get("recipient_first")
            r.recipient_last = form.cleaned_data.get("recipient_last")
            r.recipient_address = form.cleaned_data.get("recipient_address")
            r.contact_email = form.cleaned_data.get("contact_email")
            r.recipient_phone = form.cleaned_data.get("recipient_phone")
            r.zipcode = form.cleaned_data.get("zipcode")
            r.persons_in_household = form.cleaned_data.get("persons_in_household")
            r.cases_requested = form.cleaned_data.get("cases_requested")
            r.reason = form.cleaned_data.get("reason")
            r.on_behalf = form.cleaned_data.get("on_behalf")
            r.contact_first_name = form.cleaned_data.get("contact_first_name")
            r.contact_last_name = form.cleaned_data.get("contact_last_name")
            r.contact_phone = form.cleaned_data.get("contact_phone")
            r.other_supplies_needed = form.cleaned_data.get("other_supplies_needed")
            r.notes = form.cleaned_data.get("notes")
            r.save()
            
            # Build confirmation email
            from emails import confirmation_request_email_subject, confirmation_request_email_body
            confirmation_request_email_body.format(cases_requested = str(r.cases_requested),
                first_name = r.recipient_first,
                last_name = r.recipient_last,
                address = r.recipient_address,
                reason = r.reason,
                contact_email = r.contact_email)
            confirmation_request_email = (confirmation_request_email_subject, confirmation_request_email_body, settings.EMAIL_HOST_USER, [r.contact_email])
    
            # Build admin notification email
            from emails import admin_request_email_subject, admin_request_email_body
            admin_request_email_subject.format(cases_requested = str(r.cases_requested),
                first_name = r.recipient_first,
                last_name = r.recipient_last)
            admin_request_email_body.format(cases_requested = str(r.cases_requested),
                first_name = r.recipient_first,
                last_name = r.recipient_last,
                address = r.recipient_address,
                reason = r.reason)
            admin_request_email = (admin_request_email_subject, admin_request_email_body, settings.EMAIL_HOST_USER, settings.EMAIL_HOST_USER)
    
            # Send Them
            try:
                send_mass_mail((admin_request_email, confirmation_request_email), fail_silently=False)
            except:
                pass
            # Still need to check for saving of skills they have here
            return HttpResponseRedirect(reverse('request_received'))
    else:
        form = RequestDeliveryForm()
    return render(request, "request_delivery.html", {'form' : form})



def edit_request_delivery(request):
    u = get_object_or_404(User, id=request.user.id)
    r = DeliveryRequest.objects.filter(user=u).first()
    if request.method == "POST":
        form = EditRequestDeliveryForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("contact_email")
            u.first_name = form.cleaned_data.get("recipient_first")
            u.last_name = form.cleaned_data.get("recipient_last")
            u.email = email
            u.username = email
            u.save()
            r.reason = form.cleaned_data.get("reason")
            r.recipient_address = form.cleaned_data.get("recipient_address")
            r.recipient_phone = form.cleaned_data.get("recipient_phone")
            r.zipcode = form.cleaned_data.get("zipcode")
            r.persons_in_household = form.cleaned_data.get("persons_in_household")
            r.cases_requested = form.cleaned_data.get("cases_requested")
            r.reason = form.cleaned_data.get("reason")
            r.on_behalf = form.cleaned_data.get("on_behalf")
            r.contact_first_name = form.cleaned_data.get("contact_first_name")
            r.contact_last_name = form.cleaned_data.get("contact_last_name")
            r.contact_phone = form.cleaned_data.get("contact_phone")
            r.notes = form.cleaned_data.get("notes")
            r.other_supplies_needed = form.cleaned_data.get("other_supplies_needed")
            r.save()
            return HttpResponseRedirect(reverse('changes_updated'))
    else:
        userinfo = model_to_dict(u)
        requestinfo = model_to_dict(r)
        allinfo = dict(userinfo.items() + requestinfo.items() +{'recipient_first':u.first_name,'recipient_last':u.last_name, 'contact_email':u.email}.items())
        form = EditRequestDeliveryForm(initial=allinfo)
    return render(request, "edit_request_delivery.html", {'form' : form})



def organization_offer(request):
    if request.method == "POST":
        form = OrganizationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("contact_email")
            password = form.cleaned_data.get("password")
            u = User.objects.create_user(email, email, password)
            u.first_name = form.cleaned_data.get("contact_first_name")
            u.last_name = form.cleaned_data.get("contact_last_name")
            u.save()
            user = authenticate(username=email, password=password)
            login(request, user)
            u = User.objects.filter(email = email).first()

            o = Organization(contact = u)
            o.org_name = form.cleaned_data.get("org_name")
            o.address = form.cleaned_data.get("address")
            o.zipcode = form.cleaned_data.get("zipcode")
            o.phone = form.cleaned_data.get("phone")
            o.public_email = form.cleaned_data.get("public_email")
            o.website = form.cleaned_data.get("website")
            o.has_water = form.cleaned_data.get("has_water")
            o.has_volunteers =  form.cleaned_data.get("has_volunteers")
            o.has_vehicles_or_drivers =  form.cleaned_data.get("has_vehicles_or_drivers")
            o.has_testers =  form.cleaned_data.get("has_testers")
            o.has_filters =  form.cleaned_data.get("has_filters")
            o.has_wipes =  form.cleaned_data.get("has_wipes")
            o.has_vaseline =  form.cleaned_data.get("has_vaseline")
            o.has_lifting_supplies =  form.cleaned_data.get("has_lifting_supplies")
            o.has_testing_skills =  form.cleaned_data.get("has_testing_skills")
            o.has_plumbing_skills =  form.cleaned_data.get("has_plumbing_skills")
            o.has_other_supplies =  form.cleaned_data.get("has_other_supplies")
            o.other_supplies_on_hand =  form.cleaned_data.get("other_supplies_on_hand")
            o.needs_water =  form.cleaned_data.get("needs_water")
            o.needs_volunteers =  form.cleaned_data.get("needs_volunteers")
            o.needs_vehicles =  form.cleaned_data.get("needs_vehicles")
            o.needs_testers =  form.cleaned_data.get("needs_testers")
            o.needs_filters =  form.cleaned_data.get("needs_filters")
            o.needs_wipes =  form.cleaned_data.get("needs_wipes")
            o.needs_vaseline = form.cleaned_data.get("needs_vaseline")
            o.needs_lifting_supplies =  form.cleaned_data.get("needs_lifting_supplies")
            o.needs_other_supplies =  form.cleaned_data.get("needs_other_supplies")
            o.other_supplies_needed =  form.cleaned_data.get("other_supplies_needed")
            o.monday_dist_start =  form.cleaned_data.get("monday_dist_start")
            o.monday_dist_end =  form.cleaned_data.get("monday_dist_end")
            o.tuesday_dist_start =  form.cleaned_data.get("tuesday_dist_start")
            o.tuesday_dist_end =  form.cleaned_data.get("tuesday_dist_end")
            o.wednesday_dist_start =  form.cleaned_data.get("wednesday_dist_start")
            o.wednesday_dist_end =  form.cleaned_data.get("wednesday_dist_end")
            o.thursday_dist_start =  form.cleaned_data.get("thursday_dist_start")
            o.thursday_dist_end =  form.cleaned_data.get("thursday_dist_end")
            o.friday_dist_start =  form.cleaned_data.get("friday_dist_start")
            o.friday_dist_end =  form.cleaned_data.get("friday_dist_end")
            o.saturday_dist_start =  form.cleaned_data.get("saturday_dist_start")
            o.saturday_dist_end =  form.cleaned_data.get("saturday_dist_end")
            o.sunday_dist_start =  form.cleaned_data.get("sunday_dist_start")
            o.sunday_dist_end =  form.cleaned_data.get("sunday_dist_end")
            o.limits =  form.cleaned_data.get("limits")
            o.video_url =  form.cleaned_data.get("video_url")
            o.pickup_requirements =  form.cleaned_data.get("pickup_requirements")
            o.notes =  form.cleaned_data.get("notes")
            o.contractor =  form.cleaned_data.get("contractor")
            o.contractor_notes =  form.cleaned_data.get("contractor_notes")

            # Geocode the address
            address_to_code = o.address + ", " + "Flint, MI" + " "+ o.zipcode
            geolocator = GoogleV3('AIzaSyCdQa5vpC7SE5LdZAXXxGNcKJpJGmBYd6E')
            freshaddress, (o.latitude, o.longitude) = geolocator.geocode(address_to_code)
            
            o.save()
            
            # Build confirmation email
            from emails import confirmation_organization_email_subject, confirmation_organization_email_body

            needs = " "
            offering = " "
            if o.has_water == True:
                needs += "water, "
            if o.has_volunteers == True:
                needs += "volunteers, "
            if o.has_vehicles_or_drivers == True:
                needs += "water, "
            if o.has_testers == True:
                needs += "water, "
            if o.has_filters == True:
                needs += "water, "
            if o.has_wipes == True:
                needs += "water, "
            if o.has_vaseline == True:
                needs += "water, "
            if o.has_lifting_supplies == True:
                needs += "water, "
            if o.has_testing_skills == True:
                needs += "water, "
            if o.has_plumbing_skills == True:
                needs += "water, "
            if len(o.other_supplies_on_hand) > 1:
                needs += o.other_supplies_on_hand
            needs = needs.strip(", ").strip(" ")

            if o.needs_water == True:
                offering += "water, "
            if o.needs_volunteers == True:
                offering += "volunteers, "
            if o.needs_vehicles_or_drivers == True:
                offering += "water, "
            if o.needs_testers == True:
                offering += "water, "
            if o.needs_filters == True:
                offering += "water, "
            if o.needs_wipes == True:
                offering += "water, "
            if o.needs_vaseline == True:
                offering += "water, "
            if o.needs_lifting_supplies == True:
                offering += "water, "
            if len(o.other_supplies_needed) > 1:
                offering += o.other_supplies_needed
            offering = offering.strip(", ").strip(" ")

            
            confirmation_organization_email_body = confirmation_organization_email_body.format(
                contact_first_name = u.first_name,
                contact_last_name = u.last_name,
                contact_email = email,
                org_name = o.org_name,
                website = o.website,
                address = o.address,
                city = o.city,
                state = o.state,
                zipcode = o.zipcode,
                public_email = o.public_email,
                phone = o.phone,
                monday_dist_start = o.monday_dist_start,
                monday_dist_end = o.monday_dist_end,
                tuesday_dist_start = o.tuesday_dist_start,
                tuesday_dist_end = o.tuesday_dist_end,
                wednesday_dist_start = o.wednesday_dist_start,
                wednesday_dist_end = o.wednesday_dist_end,
                thursday_dist_start = o.thursday_dist_start,
                thursday_dist_end = o.thursday_dist_end,
                friday_dist_start = o.friday_dist_start,
                friday_dist_end = o.friday_dist_end,
                saturday_dist_start = o.saturday_dist_start,
                saturday_dist_end = o.saturday_dist_end,
                sunday_dist_start = o.sunday_dist_start,
                sunday_dist_end = o.sunday_dist_end,
                limits = o.limits,
                pickup_requirements = o.pickup_requirements,
                notes = o.notes,
                contractor = o.contractor,
                contractor_notes = o.contractor_notes,
                needs = needs,
                offering = offering
                )

            confirmation_organization_email = (confirmation_organization_email_subject, confirmation_organization_email_body, settings.EMAIL_HOST_USER, [email])




            # Build admin notification email
            from emails import admin_organization_email_subject, admin_organization_email_body
            admin_organization_email_subject = admin_organization_email_subject.format(
                first_name = u.first_name,
                last_name = u.last_name,
                org_name = o.org_name)
            admin_organization_email_body = admin_organization_email_body.format(
                contact_first_name = u.first_name,
                contact_last_name = u.last_name,
                contact_email = email,
                org_name = o.org_name,
                address = o.address,
                city = o.city,
                state = o.state,
                zipcode = o.zipcode,
                website = o.website,
                public_email = o.public_email,
                phone = o.phone,
                monday_dist_start = o.monday_dist_start,
                monday_dist_end = o.monday_dist_end,
                tuesday_dist_start = o.tuesday_dist_start,
                tuesday_dist_end = o.tuesday_dist_end,
                wednesday_dist_start = o.wednesday_dist_start,
                wednesday_dist_end = o.wednesday_dist_end,
                thursday_dist_start = o.thursday_dist_start,
                thursday_dist_end = o.thursday_dist_end,
                friday_dist_start = o.friday_dist_start,
                friday_dist_end = o.friday_dist_end,
                saturday_dist_start = o.saturday_dist_start,
                saturday_dist_end = o.saturday_dist_end,
                sunday_dist_start = o.sunday_dist_start,
                sunday_dist_end = o.sunday_dist_end,
                limits = o.limits,
                pickup_requirements = o.pickup_requirements,
                notes = o.notes,
                needs = needs,
                offering = offering
                )
            admin_organization_email = (admin_organization_email_subject, admin_organization_email_body, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])

            # Send Them
            try:
                send_mass_mail((admin_organization_email, confirmation_organization_email), fail_silently=False)
            except:
                pass
            # Still need to check for saving of skills they have here
            return HttpResponseRedirect(reverse('request_received'))
    else:
        form = OrganizationForm()
    return render(request, "organization_offer.html", {'form' : form})


def individual_offer(request):
    if request.method == "POST":
        form = IndividualOfferForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            u = User.objects.create_user(email, email, password)
            u.first_name = form.cleaned_data.get("first_name")
            u.last_name = form.cleaned_data.get("last_name")
            u.save()
            user = authenticate(username=email, password=password)
            login(request, user)
            u = User.objects.filter(email = email).first()

            i = IndividualHelper()
            i.user = u
            i.phone = form.cleaned_data.get("phone")
            i.address = form.cleaned_data.get("address")
            i.city = form.cleaned_data.get("city")
            if i.city=="Flint":
                i.local = True
            else:
                i.local = False

            i.state = form.cleaned_data.get("state")
            i.zipcode = form.cleaned_data.get("zipcode")
            address_to_code = i.address + ", " + i.city+", "+i.state+" "+i.zipcode
            geolocator = GoogleV3('AIzaSyCdQa5vpC7SE5LdZAXXxGNcKJpJGmBYd6E')
            freshaddress, (i.latitude, i.longitude) = geolocator.geocode(address_to_code)
            i.save()
            i = IndividualHelper.objects.filter(user = u).first()

            h = IndividualHelpOffer(individual_helper =i)
            h.wants_to_volunteer =  form.cleaned_data.get("wants_to_volunteer")
            h.group_size = form.cleaned_data.get("group_size")
            h.will_unload = form.cleaned_data.get("will_unload")
            h.will_deliver_with_vehicle = form.cleaned_data.get("will_deliver_with_vehicle")
            h.will_do_admin = form.cleaned_data.get("will_do_admin")
            h.will_do_plumbing = form.cleaned_data.get("will_do_plumbing")
            h.will_do_testing = form.cleaned_data.get("will_do_testing")
            h.other_help = form.cleaned_data.get("other_help")
            h.mon_availability_start_time = form.cleaned_data.get("mon_availability_start_time")
            h.mon_availability_end_time = form.cleaned_data.get("mon_availability_end_time")
            h.tue_availability_start_time = form.cleaned_data.get("tue_availability_start_time") 
            h.tue_availability_end_time = form.cleaned_data.get("tue_availability_end_time")
            h.wed_availability_start_time = form.cleaned_data.get("wed_availability_start_time") 
            h.wed_availability_end_time = form.cleaned_data.get("wed_availability_end_time")
            h.thu_availability_start_time = form.cleaned_data.get("thu_availability_start_time") 
            h.thu_availability_end_time = form.cleaned_data.get("thu_availability_end_time")
            h.fri_availability_start_time = form.cleaned_data.get("fri_availability_start_time") 
            h.fri_availability_end_time = form.cleaned_data.get("thu_availability_end_time")
            h.sat_availability_start_time = form.cleaned_data.get("fri_availability_start_time")
            h.sat_availability_end_time = form.cleaned_data.get("fri_availability_end_time")
            h.sun_availability_start_time = form.cleaned_data.get("sun_availability_start_time") 
            h.sun_availability_end_time = form.cleaned_data.get("sat_availability_end_time")
            h.availability_start_date = form.cleaned_data.get("availability_start_date")
            h.availability_end_date = form.cleaned_data.get("availability_end_date")
            h.availability_start_month = form.cleaned_data.get("availability_start_month")
            h.availability_end_month = form.cleaned_data.get("availability_end_month")
            h.doing_park_and_serve = form.cleaned_data.get("doing_park_and_serve")
            h.park_and_serve_address = form.cleaned_data.get("park_and_serve_address")
            h.park_and_serve_zipcode = form.cleaned_data.get("park_and_serve_zipcode")
            h.park_and_serve_month = form.cleaned_data.get("park_and_serve_month")
            h.park_and_serve_weekday = form.cleaned_data.get("park_and_serve_weekday")
            h.park_and_serve_date = form.cleaned_data.get("park_and_serve_date")
            h.park_and_serve_month = form.cleaned_data.get("park_and_serve_month")
            h.park_and_serve_items = form.cleaned_data.get("park_and_serve_items")
            h.park_and_serve_start_time = form.cleaned_data.get("park_and_serve_start_time")
            h.park_and_serve_end_time = form.cleaned_data.get("park_and_serve_end_time")
            h.video_url =  form.cleaned_data.get("video_url")
            h.notes = form.cleaned_data.get("special_instructions")
            h.save()
            
            # Build confirmation email
            from emails import confirmation_individual_email_subject, confirmation_individual_email_body
            confirmation_individual_email_body = confirmation_individual_email_body.format(
                first_name = u.first_name,
                email = email)
            confirmation_individual_email = (confirmation_individual_email_subject, confirmation_individual_email_body, settings.EMAIL_HOST_USER, [email])
    
            # Build admin notification email
            from emails import admin_individual_email_subject, admin_individual_email_body
            admin_individual_email_subject = admin_individual_email_subject.format(
                first_name = u.first_name,
                last_name = u.last_name)
            admin_individual_email_body = admin_individual_email_body.format(
                first_name = u.first_name,
                last_name = u.last_name,
                email = email,
                address = i.address,
                city = i.city,
                state = i.state,
                zipcode = i.zipcode,
                phone = i.phone,
                wants_to_volunteer = h.wants_to_volunteer,
                donated = form.cleaned_data.get("making_donation"),
                wants_to_parkandserve = form.cleaned_data.get("doing_park_and_serve"),
                )
            admin_individual_email = (admin_individual_email_subject, admin_individual_email_body, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
    
            # Send Them
            try:
                send_mass_mail((admin_individual_email, confirmation_individual_email), fail_silently=False)
            except:
                pass

            return HttpResponseRedirect(reverse('request_received'))
    else:
        form = IndividualOfferForm()
    return render(request, "individual_offer.html", {'form' : form})



@login_required
def edit_individual(request):
    u = get_object_or_404(User, id=request.user.id)
    i = IndividualHelper.objects.filter(user = u).first()
    if request.method == 'POST':
        form = EditIndividualForm(request.POST)
        if form.is_valid():
            u.first_name = form.cleaned_data.get("first_name")
            u.last_name = form.cleaned_data.get("last_name")
            u.email = form.cleaned_data.get("email")
            u.username = form.cleaned_data.get("email")
            u.save()
            i.address = form.cleaned_data.get("address")
            i.city = form.cleaned_data.get("city")
            i.phone = form.cleaned_data.get("phone")
            i.state = form.cleaned_data.get("state")
            i.zipcode = form.cleaned_data.get("zipcode")
            i.save()
            return HttpResponseRedirect(reverse('request_received'))
    else:
        userinfo = model_to_dict(u)
        indinfo = model_to_dict(i)
        allinfo = dict(userinfo.items() + indinfo.items())
        form = EditIndividualForm(initial=allinfo)
    return render(request, "edit_individual.html", {'form':form})


@login_required
def add_another_help_offer(request):
    if request.method == "POST":
        form = AddAnotherHelpOfferForm(request.POST)
        if form.is_valid():
            u = get_object_or_404(User, id = request.user.id)
            i = IndividualHelper.objects.filter(user = u).first()
            h = IndividualHelpOffer(individual_helper =i)
            h.wants_to_volunteer =  form.cleaned_data.get("wants_to_volunteer")
            h.group_size = form.cleaned_data.get("group_size")
            h.will_unload = form.cleaned_data.get("will_unload")
            h.will_deliver_with_vehicle = form.cleaned_data.get("will_deliver_with_vehicle")
            h.will_do_admin = form.cleaned_data.get("will_do_admin")
            h.will_do_plumbing = form.cleaned_data.get("will_do_plumbing")
            h.will_do_testing = form.cleaned_data.get("will_do_testing")
            h.other_help = form.cleaned_data.get("other_help")
            h.mon_availability_start_time = form.cleaned_data.get("mon_availability_start_time")
            h.mon_availability_end_time = form.cleaned_data.get("mon_availability_end_time")
            h.tue_availability_start_time = form.cleaned_data.get("tue_availability_start_time") 
            h.tue_availability_end_time = form.cleaned_data.get("tue_availability_end_time")
            h.wed_availability_start_time = form.cleaned_data.get("wed_availability_start_time") 
            h.wed_availability_end_time = form.cleaned_data.get("wed_availability_end_time")
            h.thu_availability_start_time = form.cleaned_data.get("thu_availability_start_time") 
            h.thu_availability_end_time = form.cleaned_data.get("thu_availability_end_time")
            h.fri_availability_start_time = form.cleaned_data.get("fri_availability_start_time") 
            h.fri_availability_end_time = form.cleaned_data.get("thu_availability_end_time")
            h.sat_availability_start_time = form.cleaned_data.get("fri_availability_start_time")
            h.sat_availability_end_time = form.cleaned_data.get("fri_availability_end_time")
            h.sun_availability_start_time = form.cleaned_data.get("sun_availability_start_time") 
            h.sun_availability_end_time = form.cleaned_data.get("sat_availability_end_time")
            h.availability_start_date = form.cleaned_data.get("availability_start_date")
            h.availability_end_date = form.cleaned_data.get("availability_end_date")
            h.availability_start_month = form.cleaned_data.get("availability_start_month")
            h.availability_end_month = form.cleaned_data.get("availability_end_month")
            h.doing_park_and_serve = form.cleaned_data.get("doing_park_and_serve")
            h.park_and_serve_address = form.cleaned_data.get("park_and_serve_address")
            h.park_and_serve_zipcode = form.cleaned_data.get("park_and_serve_zipcode")
            h.park_and_serve_month = form.cleaned_data.get("park_and_serve_month")
            h.park_and_serve_weekday = form.cleaned_data.get("park_and_serve_weekday")
            h.park_and_serve_date = form.cleaned_data.get("park_and_serve_date")
            h.park_and_serve_month = form.cleaned_data.get("park_and_serve_month")
            h.park_and_serve_items = form.cleaned_data.get("park_and_serve_items")
            h.park_and_serve_start_time = form.cleaned_data.get("park_and_serve_start_time")
            h.park_and_serve_end_time = form.cleaned_data.get("park_and_serve_end_time")
            h.video_url =  form.cleaned_data.get("video_url")
            h.notes = form.cleaned_data.get("special_instructions")
            h.save()
            
            # Build confirmation email
            from emails import confirmation_add_help_email_subject, confirmation_add_help_email_body
            confirmation_add_help_email_body = confirmation_add_help_email_body.format(
                first_name = u.first_name,
                email = u.email)
            confirmation_add_help_email = (confirmation_add_help_email_subject, confirmation_add_help_email_body, settings.EMAIL_HOST_USER, [u.email])

            # Build admin notification email
            from emails import admin_add_help_email_subject, admin_add_help_email_body
            admin_add_help_email_subject = admin_add_help_email_subject.format(
                first_name = u.first_name,
                last_name = u.last_name)
            admin_add_help_email_body = admin_add_help_email_body.format(
                first_name = u.first_name,
                last_name = u.last_name,
                email = u.email,
                address = i.address,
                city = i.city,
                state = i.state,
                zipcode = i.zipcode,
                phone = i.phone,
                wants_to_volunteer = h.wants_to_volunteer,
                donated = form.cleaned_data.get("making_donation"),
                wants_to_parkandserve = form.cleaned_data.get("doing_park_and_serve"))
            admin_add_help_email = (admin_add_help_email_subject, admin_add_help_email_body, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
    
            # Send Them
            try:
                send_mass_mail((admin_individual_email, confirmation_individual_email), fail_silently=False)
            except:
                pass
            # Still need to check for saving of skills they have here
            return HttpResponseRedirect(reverse('request_received'))
    else:
        form = AddAnotherHelpOfferForm()
    return render(request, "add_another_help_offer.html", {'form':form})


@login_required
def edit_organization(request):
    u = get_object_or_404(User, id=request.user.id)
    o = Organization.objects.filter(contact=u).first()
    if request.method == 'POST':
        form = EditOrganizationForm(request.POST)
        if form.is_valid():
            u.first_name = form.cleaned_data.get("contact_first_name")
            u.last_name = form.cleaned_data.get("contact_last_name")
            u.contact_email = form.cleaned_data.get("contact_email")
            u.username = form.cleaned_data.get("contact_email")
            u.save()

            o.org_name = form.cleaned_data.get("org_name")
            o.address = form.cleaned_data.get("address")
            o.zipcode = form.cleaned_data.get("zipcode")
            o.phone = form.cleaned_data.get("phone")
            o.public_email = form.cleaned_data.get("public_email")
            o.website = form.cleaned_data.get("website")
            o.has_water = form.cleaned_data.get("has_water")
            o.has_volunteers =  form.cleaned_data.get("has_volunteers")
            o.has_vehicles_or_drivers =  form.cleaned_data.get("has_vehicles_or_drivers")
            o.has_testers =  form.cleaned_data.get("has_testers")
            o.has_filters =  form.cleaned_data.get("has_filters")
            o.has_wipes =  form.cleaned_data.get("has_wipes")
            o.has_vaseline =  form.cleaned_data.get("has_vaseline")
            o.has_lifting_supplies =  form.cleaned_data.get("has_lifting_supplies")
            o.has_testing_skills =  form.cleaned_data.get("has_testing_skills")
            o.has_plumbing_skills =  form.cleaned_data.get("has_plumbing_skills")
            o.has_other_supplies =  form.cleaned_data.get("has_other_supplies")
            o.other_supplies_on_hand =  form.cleaned_data.get("other_supplies_on_hand")
            o.needs_water =  form.cleaned_data.get("needs_water")
            o.needs_volunteers =  form.cleaned_data.get("needs_volunteers")
            o.needs_vehicles =  form.cleaned_data.get("needs_vehicles")
            o.needs_testers =  form.cleaned_data.get("needs_testers")
            o.needs_filters =  form.cleaned_data.get("needs_filters")
            o.needs_wipes =  form.cleaned_data.get("needs_wipes")
            o.needs_vaseline = form.cleaned_data.get("needs_vaseline")
            o.needs_lifting_supplies =  form.cleaned_data.get("needs_lifting_supplies")
            o.needs_other_supplies =  form.cleaned_data.get("needs_other_supplies")
            o.other_supplies_needed =  form.cleaned_data.get("other_supplies_needed")
            o.monday_dist_start =  form.cleaned_data.get("monday_dist_start")
            o.monday_dist_end =  form.cleaned_data.get("monday_dist_end")
            o.tuesday_dist_start =  form.cleaned_data.get("tuesday_dist_start")
            o.tuesday_dist_end =  form.cleaned_data.get("tuesday_dist_end")
            o.wednesday_dist_start =  form.cleaned_data.get("wednesday_dist_start")
            o.wednesday_dist_end =  form.cleaned_data.get("wednesday_dist_end")
            o.thursday_dist_start =  form.cleaned_data.get("thursday_dist_start")
            o.thursday_dist_end =  form.cleaned_data.get("thursday_dist_end")
            o.friday_dist_start =  form.cleaned_data.get("friday_dist_start")
            o.friday_dist_end =  form.cleaned_data.get("friday_dist_end")
            o.saturday_dist_start =  form.cleaned_data.get("saturday_dist_start")
            o.saturday_dist_end =  form.cleaned_data.get("saturday_dist_end")
            o.sunday_dist_start =  form.cleaned_data.get("sunday_dist_start")
            o.sunday_dist_end =  form.cleaned_data.get("sunday_dist_end")
            o.limits =  form.cleaned_data.get("limits")
            o.video_url =  form.cleaned_data.get("video_url")
            o.pickup_requirements =  form.cleaned_data.get("pickup_requirements")
            o.contractor =  form.cleaned_data.get("contractor")
            o.contractor_notes =  form.cleaned_data.get("contractor_notes")
            o.notes =  form.cleaned_data.get("notes")
            o.save()
            return HttpResponseRedirect(reverse('changes_updated'))
        else:
            return render(request, "edit_organization.html", {'form':form})
    else:
        userinfo = model_to_dict(u)
        orginfo = model_to_dict(o)
        allinfo = dict(userinfo.items() + orginfo.items() +{'contact_first_name':u.first_name,'contact_last_name':u.last_name, 'contact_email':u.email}.items())
        form = EditOrganizationForm(initial=allinfo)
        return render(request, "edit_organization.html", {'form':form})