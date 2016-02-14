import django
django.setup()
from app.models import *
from django.contrib.auth.models import User
from django.utils import timezone
from geopy.geocoders import GoogleV3


WaterDistributionLocation.objects.all().delete()


# Add basic info
antioch = WaterDistributionLocation(name = "Antioch Missionary Baptists Church", address = "1401 E Stewart Ave", zipcode = "48505", phone = "810 785-4060", limits = "4 cases per person", region = "North", tuesday_dist = "10am-2pm", friday_dist = "10am-2pm")
azusa = WaterDistributionLocation(name = "Greater Friendship Azusa Ministries COGIC", address = "Detroit Street", zipcode = "48505", phone = "810 785-6000", limits = "Take what you need", region = "North")
bethel = WaterDistributionLocation(name = "Bethel United Methodist Church", address = "1309 N Ballenger Hwy", zipcode = "48504", phone = "810 238-3843", region = "North")
joy = WaterDistributionLocation(name = "Joy Tabernacle Church", address = "2505 N Chevrolet Ave", zipcode = "48504", phone = "810 234-8790", region = "North", limits = "Take what you need", saturday_dist = "Feb 13, 11am-4pm")
holy = WaterDistributionLocation(name = "Greater Holy Temple", address = "6702 N Dort Hwy", zipcode = "48505", region = "North")

antioch.save()
azusa.save()
bethel.save()
joy.save()
holy.save()


# Add geocode
locations = WaterDistributionLocation.objects.all()

for location in locations:
    address_to_code = location.address + ", " + location.city + ", " + location.state + " "+ location.zipcode
    geolocator = GoogleV3()
    address, (location.latitude, location.longitude) = geolocator.geocode(address_to_code)
    print location.latitude
    location.save()

