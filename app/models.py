from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    contact = models.ForeignKey(User)
    org_name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)    
    city = models.CharField(max_length=45, default = "Flint")
    state = models.CharField(max_length=4, default = "MI")
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)


class ResourceLocation(models.Model):
    organization = models.ForeignKey(Organization)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=45, default = "Flint")
    state = models.CharField(max_length=4, default = "MI")
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.FloatField(default = -83.6874562)
    latitude = models.FloatField(default = 43.0125274)
    has_water = models.IntegerField(null=True, blank=True)
    has_volunteers = models.IntegerField(null=True, blank=True)
    has_vehicles_or_drivers = models.IntegerField(null=True, blank=True)
    testers = models.IntegerField(null=True, blank=True)
    has_lifting_supplies = models.IntegerField(null=True, blank=True)
    has_other_supplies = models.IntegerField(null=True, blank=True)
    other_supplies = models.TextField()
    monday_dist = models.CharField(max_length=200, null=True, blank=True)
    tuesday_dist = models.CharField(max_length=200, null=True, blank=True)
    wednesday_dist = models.CharField(max_length=200, null=True, blank=True)
    thursday_dist = models.CharField(max_length=200, null=True, blank=True)
    friday_dist = models.CharField(max_length=200, null=True, blank=True)
    saturday_dist = models.CharField(max_length=200, null=True, blank=True)
    sunday_dist = models.CharField(max_length=200, null=True, blank=True)
    water_case_limit = models.CharField(max_length=200, null=True, blank=True)
    requirements = models.CharField(max_length=200, null=True, blank=True)
    date_added = models.DateTimeField('date added', null=True, blank=True)
    notes = models.TextField(null=True, blank=True)


class IndividualHelper(models.Model):
    user = models.ForeignKey(User)
    user_type = models.IntegerField(default = 1)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=4, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    local = models.IntegerField(null=True, blank=True)


class HelpOffer(models.Model):
    cases_count = models.IntegerField(null=True, blank=True)
    pallets_count = models.IntegerField(null=True, blank=True)
    back_braces_count = models.IntegerField(null=True, blank=True)
    dollies_count = models.IntegerField(null=True, blank=True)
    vaseline_count = models.IntegerField(null=True, blank=True)
    wipes_count = models.IntegerField(null=True, blank=True)
    dollar_donation_amount = models.FloatField(null=True, blank=True)
    total_amount = models.FloatField(null=True, blank=True)
    volunteer_interest = models.IntegerField(null=True, blank=True)
    group_size = models.IntegerField(null=True, blank=True)
    will_unload = models.IntegerField(null=True, blank=True)
    will_deliver = models.IntegerField(null=True, blank=True)
    have_vehicle = models.IntegerField(null=True, blank=True)
    availability = models.TextField(null=True, blank=True)
    park_and_serve_address_in_flint = models.CharField(max_length=200, null=True, blank=True)
    park_and_serve_date_and_time = models.CharField(max_length=200, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)


class DeliveryDate(models.Model):
    date = models.DateTimeField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    volunteers_needed = models.IntegerField(null=True, blank=True)
    volunteers_scheduled = models.IntegerField(null=True, blank=True)
    vehicles_needed = models.IntegerField(null=True, blank=True)
    vehicles_scheduled = models.IntegerField(null=True, blank=True)
    cases_to_deliver = models.IntegerField(null=True, blank=True)
    cases_delivered = models.IntegerField(null=True, blank=True)
    filters_to_deliver = models.IntegerField(null=True, blank=True)
    filters_delivered = models.IntegerField(null=True, blank=True)
    wipes_to_deliver = models.IntegerField(null=True, blank=True)
    wipes_delivered = models.IntegerField(null=True, blank=True)
    vaseline_to_deliver = models.IntegerField(null=True, blank=True)
    vaseline_delivered = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)


class DeliveryRequest(models.Model):
    first_name = models.CharField(max_length=45, null=True, blank=True)
    last_name = models.CharField(max_length=45, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    longitude = models.FloatField(default = -83.6874562)
    latitude = models.FloatField(default = 43.0125274)
    delivery_date = models.ForeignKey(DeliveryDate)
    persons_in_household = models.IntegerField(null=True, blank=True)
    cases_requested = models.IntegerField(null=True, blank=True)
    filters_requested = models.IntegerField(null=True, blank=True)
    vaseline_requested = models.IntegerField(null=True, blank=True)
    wipes_requested = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)




########Unused for now############################



class ServiceQuestionnaire(models.Model):
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    first_time_getting_water = models.IntegerField(null=True, blank=True)
    trips_per_week = models.IntegerField(null=True, blank=True)
    household_weekly_cases = models.IntegerField(null=True, blank=True)
    best_experiences = models.TextField(null=True, blank=True)
    worst_experiences = models.TextField(null=True, blank=True)
    wait_time = models.TextField(null=True, blank=True)
    know_of_others = models.TextField(null=True, blank=True)
    changes = models.TextField(null=True, blank=True)
    video_url = models.CharField(max_length=20, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)


class WaterDistributionLocation(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=45, default = "Flint")
    state = models.CharField(max_length=4, default = "MI")
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    region = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.FloatField(default = -83.6874562)
    latitude = models.FloatField(default = 43.0125274)
    monday_dist = models.CharField(max_length=200, null=True, blank=True)
    tuesday_dist = models.CharField(max_length=200, null=True, blank=True)
    wednesday_dist = models.CharField(max_length=200, null=True, blank=True)
    thursday_dist = models.CharField(max_length=200, null=True, blank=True)
    friday_dist = models.CharField(max_length=200, null=True, blank=True)
    saturday_dist = models.CharField(max_length=200, null=True, blank=True)
    sunday_dist = models.CharField(max_length=200, null=True, blank=True)
    limits = models.CharField(max_length=200, null=True, blank=True)
    date_added = models.DateTimeField('date added', null=True, blank=True)
    notes = models.TextField(null=True, blank=True)