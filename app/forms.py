from django import forms
from app.models import *
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from datetime import date


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



class RequestDeliveryForm(forms.Form):
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.CharField(max_length=45)
    phone = forms.CharField(max_length=14)


class IndividualOfferForm(forms.Form):
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.CharField(max_length=45)
    phone = forms.CharField(max_length=14)


class OrganizationForm(forms.Form):
    org_name = forms.CharField(max_length=45)
    contact_first_name = forms.CharField(max_length=45)
    contact_last_name = forms.CharField(max_length=45)
    email = forms.CharField(max_length=45)
    phone = forms.CharField(max_length=14)


# We present seven of these together at first registration, each one is horizontally inline displayed
class DistributionEventForm(forms.Form):
    weekday = forms.ChoiceField(choices = DAYS_OF_WEEK)
    month = forms.ChoiceField(choices = MONTHS)
    start_date = forms.CharField(max_length=2, initial = date.today())
    end_date = forms.CharField(max_length=2, initial = date.today().replace(year = date.today().year + 1))
    start_time = forms.ChoiceField(choices = TIMES)
    end_time = forms.ChoiceField(choices = TIMES)
    recurring = forms.ChoiceField(choices = RECURRENCE)