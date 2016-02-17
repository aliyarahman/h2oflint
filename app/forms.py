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
    ('10:30am', '11:30am'),
    ('11:00am','12:00am' ),
    ('11:30am', '12:30am'),
)



class OrganizationForm(forms.Form):
    contact_first_name = forms.CharField(max_length=45)
    contact_last_name = forms.CharField(max_length=45)
    email = forms.CharField(max_length=45)
    password = forms.CharField(max_length=24)
    retype_password = forms.CharField(max_length=24)
    org_name = forms.CharField(max_length=45)
    address = forms.CharField(max_length=200)
    city = forms.CharField(max_length=45, initial = "Flint")
    state = forms.CharField(max_length=4, initial = "MI")
    zipcode = forms.CharField(max_length=10)
    longitude = forms.FloatField()
    latitude = forms.FloatField()
    phone = forms.CharField(max_length=14)
    org_email = forms.CharField(max_length=200)
    website = forms.CharField(max_length=200)
    monday_start_time = forms.ChoiceField(choices = TIMES)
    monday_end_time = forms.ChoiceField(choices = TIMES)
    tuesday_start_time = forms.ChoiceField(choices = TIMES)
    tuesday_end_time = forms.ChoiceField(choices = TIMES)
    wednesday_start_time = forms.ChoiceField(choices = TIMES)
    wednesday_end_time = forms.ChoiceField(choices = TIMES)
    thursday_start_time = forms.ChoiceField(choices = TIMES)
    thursday_end_time = forms.ChoiceField(choices = TIMES)
    friday_start_time = forms.ChoiceField(choices = TIMES)
    friday_end_time = forms.ChoiceField(choices = TIMES)
    saturday_start_time = forms.ChoiceField(choices = TIMES)
    saturday_end_time = forms.ChoiceField(choices = TIMES)
    sunday_start_time = forms.ChoiceField(choices = TIMES)
    sunday_end_time = forms.ChoiceField(choices = TIMES)
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


class H2OFlintDeliveryDate(forms.Form):
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
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.CharField(max_length=45)
    phone = forms.CharField(max_length=14)



class DeliveryRequest(forms.Form):
    delivery_date = forms.CharField(initial=1)
    recipient_first = forms.CharField(max_length=45)
    recipient_last = forms.CharField(max_length=45)
    recipient_address = forms.CharField(max_length=200)
    longitude = forms.FloatField(initial = -83.6874562)
    latitude = forms.FloatField(initial = 43.0125274)
    recipient_phone = forms.CharField(max_length=20)
    zipcode = forms.CharField(max_length=10)
    persons_in_household = forms.IntegerField()
    cases_requested = forms.IntegerField()
    on_behalf = forms.BooleanField()
    contact_first_name = forms.CharField(max_length=45)
    contact_last_name = forms.CharField(max_length=45)
    contact_email = forms.CharField(max_length=200)
    contact_phone = forms.CharField(max_length=20)
    other_supplies_needed = forms.CharField(widget=forms.Textarea)


class IndividualOfferForm(forms.Form):
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.CharField(max_length=45)
    phone = forms.CharField(max_length=14)