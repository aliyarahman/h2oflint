import django
django.setup()
from app.models import *
from django.contrib.auth.models import User
from django.utils import timezone
from geopy.geocoders import GoogleV3
import csv


# Pull up users since these will be needed to create
try:
    dev = User.objects.create_superuser(username="dev@h2oflint.com", email = "dev@h2oflint.com", password = "waterisahumanright", first_name = "Aliya", last_name = "Rahman")
    dev.save()
except:
    pass
dev = User.objects.filter(username="dev@h2oflint.com").first()

try:
    darnell = User.objects.create_superuser(username="darnell@h2oflint.com", email = "darnell@h2oflint.com", password = "parney37", first_name = "Darnell", last_name = "Ishmel")
    darnell.save()
except:
    pass
darnell = User.objects.filter(username="darnell@h2oflint.com").first()


try:
    sam = User.objects.create_superuser(username="sam@h2oflint.com", email = "sam@h2oflint.com", password = "waterisahumanright", first_name = "Samantha", last_name = "Parsons")
    sam.save()
except:
    pass
sam = User.objects.filter(username="sam@h2oflint.com").first()



# Add organizations with their regular distribution schedules

Organization.objects.all().delete()

with open('distributions.csv', 'rbU') as csvfile:
    organizations = csv.DictReader(csvfile, delimiter=',', quotechar='"')

    for index, row in enumerate(organizations):
        print row

        name = row['name'].strip()
        address = row['address'].strip()
        city = row['city'].strip()
        state = row['state'].strip()
        zipcode = row['zipcode'].strip()
        phone = row['phone'].strip()
        website = row['website'].strip()
        email = row['email'].strip()
        limits = row['limits'].strip()
        mon_dist_start = row['monday_dist'].split("-")[0]
        try:
            mon_dist_end = row['monday_dist'].split("-")[1]
        except: 
            mon_dist_end = ""
        tue_dist_start = row['tuesday_dist'].split("-")[0]
        try:
            tue_dist_end = row['tuesday_dist'].split("-")[1]
        except: 
            tue_dist_end = ""
        wed_dist_start = row['wednesday_dist'].split("-")[0]
        try:
            wed_dist_end = row['wednesday_dist'].split("-")[1]
        except: 
            wed_dist_end = ""
        thu_dist_start = row['thursday_dist'].split("-")[0]
        try:
            thu_dist_end = row['thursday_dist'].split("-")[1]
        except: 
            thu_dist_end = ""
        fri_dist_start = row['friday_dist'].split("-")[0]
        try:
            fri_dist_end = row['friday_dist'].split("-")[1]
        except: 
            fri_dist_end = ""
        sat_dist_start = row['saturday_dist'].split("-")[0]
        try:
            sat_dist_end = row['saturday_dist'].split("-")[1]
        except: 
            sat_dist_end = ""
        sun_dist_start = row['sunday_dist'].split("-")[0]
        try:
            sun_dist_end = row['sunday_dist'].split("-")[1]
        except: 
            sun_dist_end = ""
        


        address_to_code = address + ", " + city + ", " + state + " "+ zipcode
        geolocator = GoogleV3()
        freshaddress, (latitude, longitude) = geolocator.geocode(address_to_code)

        o = Organization(contact = dev, org_name = name, address=address, city=city, state=state, zipcode=zipcode, phone=phone, website=website, email=email, latitude=latitude, longitude=longitude, has_water=True, monday_dist_start = mon_dist_start, monday_dist_end = mon_dist_end, tuesday_dist_start = tue_dist_start, tuesday_dist_end = tue_dist_end, wednesday_dist_start = wed_dist_start, wednesday_dist_end = wed_dist_end, thursday_dist_start = thu_dist_start, thursday_dist_end = thu_dist_end, friday_dist_start = fri_dist_start, friday_dist_end = fri_dist_end, saturday_dist_start = sat_dist_start, saturday_dist_end = sat_dist_end, sunday_dist_start = sun_dist_start, sunday_dist_end = sun_dist_end, date_created=timezone.now())


        o.save()