from django import forms
from app.models import *
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from datetime import date
from django.utils import timezone
import calendar


DAYS_OF_WEEK = (
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
    ('Sun', 'Sunday'),
)

YESNO = (
    (True, 'Yes'),
    (False, 'No'),
)

MONTHS = (
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December'),
)

RECURRENCE = (
    (0, 'Never'),
    (1, 'Every week'),
    (2, 'Every two weeks'),
    (3, 'Once a month'),
)

MONTHS = (
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (4, 'April'),
    (5, 'May'),
    (6, 'June'),
    (7, 'July'),
    (8, 'August'),
    (9, 'September'),
    (10, 'October'),
    (11, 'November'),
    (12, 'December'),
)

TIMES = (
    ('', ''),
    ('None', 'None yet' ),
    ('12:00am','12:00am' ),
    ('12:30am', '12:30am'),
    ('1:00am','1:00am' ),
    ('1:30am', '1:30am'),
    ('2:00am','2:00am' ),
    ('2:30am', '2:30am'),
    ('3:00am','3:00am' ),
    ('3:30am', '3:30am'),
    ('4:00am','4:00am' ),
    ('4:30am', '4:30am'),
    ('5:00am','5:00am' ),
    ('5:30am', '5:30am'),
    ('6:00am','6:00am' ),
    ('6:30am', '6:30am'),
    ('7:00am','7:00am' ),
    ('7:30am', '7:30am'),
    ('8:00am','8:00am' ),
    ('8:30am', '8:30am'),
    ('9:00am','9:00am' ),
    ('9:30am', '9:30am'),
    ('10:00am','10:00am' ),
    ('10:30am', '10:30am'),
    ('11:00am','11:00am' ),
    ('11:30am', '11:30am'),
    ('12:00pm','12:00pm' ),
    ('12:30pm', '12:30pm'),
    ('1:00pm','1:00pm' ),
    ('1:30pm', '1:30pm'),
    ('2:00pm','2:00pm' ),
    ('2:30pm', '2:30pm'),
    ('3:00pm','3:00pm' ),
    ('3:30pm', '3:30pm'),
    ('4:00pm','4:00pm' ),
    ('4:30pm', '4:30pm'),
    ('5:00pm','5:00pm' ),
    ('5:30pm', '5:30pm'),
    ('6:00pm','6:00pm' ),
    ('6:30pm', '6:30pm'),
    ('7:00pm','7:00pm' ),
    ('7:30pm', '7:30pm'),
    ('8:00pm','8:00pm' ),
    ('8:30pm', '8:30pm'),
    ('9:00pm','9:00pm' ),
    ('9:30pm', '9:30pm'),
    ('10:00pm','10:00pm' ),
    ('10:30pm', '10:30pm'),
    ('11:00pm','11:00pm' ),
    ('11:30pm', '11:30pm'),
)



class OrganizationForm(forms.Form):
    contact_first_name = forms.CharField(max_length=45)
    contact_last_name = forms.CharField(max_length=45)
    contact_email = forms.CharField(max_length=45)
    password = forms.CharField(widget=forms.PasswordInput())
    retype_password = forms.CharField(widget=forms.PasswordInput())
    org_name = forms.CharField(max_length=45)
    address = forms.CharField(max_length=200)
    city = forms.CharField(max_length=45)
    state = forms.CharField(max_length=4)
    zipcode = forms.CharField(max_length=10)
    phone = forms.CharField(max_length=14)
    public_email = forms.CharField(max_length=200, required=False)
    website = forms.CharField(max_length=200, required=False)
    monday_dist_start = forms.ChoiceField(choices = TIMES, required=False)
    monday_dist_end = forms.ChoiceField(choices = TIMES, required=False)
    tuesday_dist_start = forms.ChoiceField(choices = TIMES, required=False)
    tuesday_dist_end = forms.ChoiceField(choices = TIMES, required=False)
    wednesday_dist_start = forms.ChoiceField(choices = TIMES, required=False)
    wednesday_dist_end = forms.ChoiceField(choices = TIMES, required=False)
    thursday_dist_start = forms.ChoiceField(choices = TIMES, required=False)
    thursday_dist_end = forms.ChoiceField(choices = TIMES, required=False)
    friday_dist_start = forms.ChoiceField(choices = TIMES, required=False)
    friday_dist_end = forms.ChoiceField(choices = TIMES, required=False)
    saturday_dist_start = forms.ChoiceField(choices = TIMES, required=False)
    saturday_dist_end = forms.ChoiceField(choices = TIMES, required=False)
    sunday_dist_start = forms.ChoiceField(choices = TIMES, required=False)
    sunday_dist_end = forms.ChoiceField(choices = TIMES, required=False)
    has_water = forms.BooleanField(required=False, initial=False)
    has_volunteers = forms.BooleanField(required=False, initial=False)
    has_vehicles_or_drivers = forms.BooleanField(required=False, initial=False)
    has_filters = forms.BooleanField(required=False, initial=False)
    has_testers = forms.BooleanField(required=False, initial=False)
    has_wipes = forms.BooleanField(required=False, initial=False)
    has_vaseline = forms.BooleanField(required=False, initial=False)
    has_lifting_supplies = forms.BooleanField(required=False, initial=False)
    has_testing_skills = forms.BooleanField(required=False, initial=False)
    has_plumbing_skills = forms.BooleanField(required=False, initial=False)
    has_other_supplies = forms.BooleanField(required=False, initial=False)
    other_supplies_on_hand = forms.CharField(widget=forms.Textarea, required=False)
    needs_water = forms.BooleanField(required=False)
    needs_volunteers = forms.BooleanField(required=False)
    needs_vehicles_or_drivers = forms.BooleanField(required=False)
    needs_filters = forms.BooleanField(required=False)
    needs_testers = forms.BooleanField(required=False)
    needs_wipes = forms.BooleanField(required=False)
    needs_vaseline = forms.BooleanField(required=False)
    needs_lifting_supplies = forms.BooleanField(required=False)
    needs_other_supplies = forms.BooleanField(required=False)
    other_supplies_needed = forms.CharField(widget=forms.Textarea, required=False)
    limits = forms.CharField(max_length=140, required=False)
    pickup_requirements = forms.CharField(max_length=140, required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False)


# For special events not covered by the regular distribution schedule in organization form
class DistributionEventForm(forms.Form):
    weekday = forms.ChoiceField(choices = DAYS_OF_WEEK)
    month = forms.ChoiceField(choices = MONTHS)
    date = forms.CharField(max_length=2, initial = date.today())
    start_time = forms.ChoiceField(choices = TIMES)
    end_time = forms.ChoiceField(choices = TIMES)
    recurring = forms.ChoiceField(choices = RECURRENCE)
    has_water = forms.BooleanField()
    has_volunteers = forms.BooleanField()
    has_vehicles_or_drivers = forms.BooleanField()
    has_filters = forms.BooleanField()
    has_testers = forms.BooleanField()
    has_lifting_supplies = forms.BooleanField()
    has_other_supplies = forms.BooleanField()
    other_supplies_on_hand = forms.CharField(widget=forms.Textarea)
    needs_water = forms.BooleanField()
    needs_volunteers = forms.BooleanField()
    needs_vehicles_or_drivers = forms.BooleanField()
    needs_filters = forms.BooleanField()
    needs_testers = forms.BooleanField()
    needs_lifting_supplies = forms.BooleanField()
    needs_other_supplies = forms.BooleanField()
    other_supplies_needed = forms.CharField(widget=forms.Textarea)



class AddDeliveryDateForm(forms.Form):
    month = forms.CharField(max_length=9, initial=timezone.now().month)
    weekday = forms.CharField(max_length=9, initial=calendar.day_name[date.today().weekday()])
    date = forms.CharField(max_length=2, )
    year = forms.CharField(max_length=4, initial=timezone.now().year)
    start_time = forms.CharField(max_length=8)
    end_time = forms.CharField(max_length=8)
    volunteers_needed = forms.IntegerField()
    volunteers_scheduled = forms.IntegerField()
    vehicles_needed = forms.IntegerField()
    vehicles_scheduled = forms.IntegerField()
    cases_to_deliver = forms.IntegerField()
    cases_delivered = forms.IntegerField()
    filters_to_deliver = forms.IntegerField()
    filters_delivered = forms.IntegerField()
    wipes_to_deliver = forms.IntegerField()
    wipes_delivered = forms.IntegerField()
    vaseline_to_deliver = forms.IntegerField()
    vaseline_delivered = forms.IntegerField()
    other_supplies_needed = forms.CharField(widget=forms.Textarea)


class H2OFlintDeliveryDateForm(forms.Form):
    month = forms.CharField(max_length=20, )
    date = forms.CharField(max_length=20, )
    year = forms.CharField(max_length=4, initial="2016")
    start_time = forms.CharField(max_length=8)
    end_time = forms.CharField(max_length=8)
    volunteers_needed = forms.IntegerField()
    volunteers_scheduled = forms.IntegerField()
    vehicles_needed = forms.IntegerField()
    vehicles_scheduled = forms.IntegerField()
    cases_to_deliver = forms.IntegerField()
    cases_delivered = forms.IntegerField()
    filters_to_deliver = forms.IntegerField()
    filters_delivered = forms.IntegerField()
    wipes_to_deliver = forms.IntegerField()
    wipes_delivered = forms.IntegerField()
    vaseline_to_deliver = forms.IntegerField()
    vaseline_delivered = forms.IntegerField()
    other_supplies_needed = forms.CharField(widget=forms.Textarea)

class RequestDeliveryForm(forms.Form):
    delivery_date = forms.ModelChoiceField(queryset= H2OFlintDeliveryDate.objects.all())
    recipient_first = forms.CharField(max_length=45)
    recipient_last = forms.CharField(max_length=45)
    recipient_address = forms.CharField(max_length=200)
    recipient_phone = forms.CharField(max_length=20)
    zipcode = forms.CharField(max_length=10)
    persons_in_household = forms.IntegerField()
    cases_requested = forms.IntegerField()
    contact_first_name = forms.CharField(max_length=45)
    contact_last_name = forms.CharField(max_length=45)
    contact_email = forms.CharField(max_length=200)
    contact_phone = forms.CharField(max_length=20)
    other_supplies_needed = forms.CharField(widget=forms.Textarea)
    notes = forms.CharField(widget=forms.Textarea)


class IndividualOfferForm(forms.Form):
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.CharField(max_length=45)
    phone = forms.CharField(max_length=14)
    address = forms.CharField(max_length=200)
    city = forms.CharField(max_length=45)
    state = forms.CharField(max_length=4)
    zipcode = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput())
    retype_password = forms.CharField(widget=forms.PasswordInput())
    wants_to_volunteer = forms.ChoiceField(choices = YESNO)
    group_size = forms.IntegerField(initial=0, required=False)
    will_unload = forms.BooleanField(initial= False, required=False)
    will_deliver_with_vehicle = forms.BooleanField(initial = False, required=False)
    will_do_admin = forms.BooleanField(initial = False, required=False)
    will_do_testing = forms.BooleanField(initial = False, required=False)
    will_do_plumbing = forms.BooleanField(initial = False, required=False)
    mon_availability_start_time = forms.ChoiceField(choices = TIMES, required=False)
    mon_availability_end_time = forms.ChoiceField(choices = TIMES, required=False)
    tue_availability_start_time = forms.ChoiceField(choices = TIMES, required=False)
    tue_availability_end_time = forms.ChoiceField(choices = TIMES, required=False)
    wed_availability_start_time = forms.ChoiceField(choices = TIMES, required=False)
    wed_availability_end_time = forms.ChoiceField(choices = TIMES, required=False)
    thu_availability_start_time = forms.ChoiceField(choices = TIMES, required=False)
    thu_availability_end_time = forms.ChoiceField(choices = TIMES, required=False)
    fri_availability_start_time = forms.ChoiceField(choices = TIMES, required=False)
    fri_availability_end_time = forms.ChoiceField(choices = TIMES, required=False)
    sat_availability_start_time = forms.ChoiceField(choices = TIMES, required=False)
    sat_availability_end_time = forms.ChoiceField(choices = TIMES, required=False)
    sun_availability_start_time = forms.ChoiceField(choices = TIMES, required=False)
    sun_availability_end_time = forms.ChoiceField(choices = TIMES, required=False)
    availability_start_date = forms.CharField(required=False)
    availability_end_date = forms.CharField(required=False)
    availability_start_month = forms.ChoiceField(choices = MONTHS, required=False)
    availability_end_month = forms.ChoiceField(choices = MONTHS, required=False)
    availability_start_year = forms.ChoiceField(choices = TIMES, required=False)
    availability_end_year = forms.ChoiceField(choices = TIMES, required=False)
    cases_count = forms.IntegerField(initial=0, required=False)
    pallets_count = forms.IntegerField(initial=0, required=False)
    back_braces_count = forms.IntegerField(initial=0, required=False)
    dollies_count = forms.IntegerField(initial=0, required=False)
    vaseline_count = forms.IntegerField(initial=0, required=False)
    wipes_count = forms.IntegerField(initial=0, required=False)
    dollar_donation_amount = forms.IntegerField(initial=0, required=False)
    doing_park_and_serve = forms.ChoiceField(choices = YESNO, required=False)
    park_and_serve_address = forms.CharField(max_length=200, required=False)
    park_and_serve_zipcode = forms.CharField(max_length=10, required=False)
    park_and_serve_month = forms.ChoiceField(choices = MONTHS, required=False)
    park_and_serve_weekday = forms.ChoiceField(choices = DAYS_OF_WEEK, required=False)
    park_and_serve_date = forms.CharField(max_length=2, required=False)
    park_and_serve_start_time = forms.ChoiceField(choices = TIMES, required=False)
    park_and_serve_items = forms.CharField(max_length=140, required=False)
    park_and_serve_end_time = forms.ChoiceField(choices = TIMES, required=False)
    special_instructions = forms.CharField(widget=forms.Textarea, max_length=140, required=False)
    note_for_recipient = forms.CharField(widget=forms.Textarea, max_length=1000, required=False)