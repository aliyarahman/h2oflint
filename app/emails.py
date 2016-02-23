# Individual delivery request emails

confirmation_request_email_subject = "We've received your water delivery request"
confirmation_request_email_body = '''Thanks for submitting a delivery request at H2OFlint!

Here are the details of your request:
    Cases of water requested: {cases_requested}
    Recipient: {first_name} {last_name}
    Address: {address}
    Reason: {reason}

After we've reviewed your request, a volunteer will contact you.

You can log back into the site any time to update your information by using {contact_email} as your username and the password you created when you submitted this request.

If you have questions, please email help@h2oflint.com.

Thank you!

H2Oflint

'''

admin_request_email_subject = '''Water delivery request from {first_name} {last_name}'''
admin_request_email_body = '''
Hi {first_name},

Thanks for submitting a delivery request at H2OFlint!

Here are the details of the request:
    Cases of water requested: {cases_requested}
    Recipient: {first_name} {last_name}
    Address: {address}
    Reason: {reason}

'''

# ========================================================
# Organization offers or requests for help

confirmation_organization_email_subject = "Thanks for signing up your organization on H2OFlint"
confirmation_organization_email_body = '''
Hi {contact_first_name},

Thanks for registering {org_name} to give or receive help through H2OFlint. As soon as one of our administrators has checked your request, your location will start to show up on our map and list of distribution centers so that others can find you!

You can log back into the site any time to update your information by using {contact_email} as your username and the password you created when you submitted this request.

Thanks for using our site - your request details are below!
------------------------

Here's a copy of the info we received:

Organization: {org_name}
Address: {address}, {city}, {state} {zipcode}
Phone: {phone}
Website: {website}
Public email: {public_email}

Your distribution schedule:
Monday: {monday_dist_start} - {monday_dist_end}
Tuesday: {tuesday_dist_start} - {tuesday_dist_end}
Wednesday: {wednesday_dist_start} - {wednesday_dist_end}
Thursday: {thursday_dist_start} - {thursday_dist_end}
Friday: {friday_dist_start} - {friday_dist_end}
Saturday: {saturday_dist_start} - {saturday_dist_end}
Sunday: {sunday_dist_start} - {sunday_dist_end}

You are offering: {offering}

You need: {needs}

Case limit for water pickups: {limits}
Pickup requirements: {pickup_requirements}
Additional notes: {notes}
'''



admin_organization_email_subject = '''We just received an organization registration for {org_name}'''
admin_organization_email_body =  '''
{contact_first_name} {contact_last_name} ({contact_email}) has just registered {org_name} through H2OFlint.

Please log on to review and approve this location so it can be added to the map and search results.

------------------------

Here's a copy of the info we received:

Organization: {org_name}
Address: {address}, {city}, {state} {zipcode}
Phone: {phone}
Website: {website}
Public email {public_email}

Your distribution schedule:
Monday: {monday_dist_start} - {monday_dist_end}
Tuesday: {tuesday_dist_start} - {tuesday_dist_end}
Wednesday: {wednesday_dist_start} - {wednesday_dist_end}
Thursday: {thursday_dist_start} - {thursday_dist_end}
Friday: {friday_dist_start} - {friday_dist_end}
Saturday: {saturday_dist_start} - {saturday_dist_end}
Sunday: {sunday_dist_start} - {sunday_dist_end}

Is offering: {offering}

Needs: {needs}

Case limit for water pickups: {limits}
Pickup requirements: {pickup_requirements}
Additional notes: {notes}
'''


#==============================================
# Individiual offers of help

confirmation_individual_email_subject = "Thanks for offering to help through H2OFlint!"
confirmation_individual_email_body = '''Hi {first_name},

Thanks for registering to help through H2OFlint!

You can log back into the site any time to update your information by using {email} as your username and the password you created when you registered.

Thanks for using our site!

- H20Flint
'''


admin_individual_email_subject = "We've received an individual signup from {first_name} {last_name}."

admin_individual_email_body = '''
We just received an individual helper registration for {first_name} {last_name}

Their info is:
------------------
email: {email}
Address: {address}, {city}, {state} {zipcode}
Phone: {phone}

Type of help:
Volunteer: {wants_to_volunteer}
Donate: {donated}
Park and serve: {wants_to_parkandserve}

'''



#==============================================
# Individiual offers of help

confirmation_add_help_email_subject = "Thanks for offering more help through H2OFlint"
confirmation_add_help_email_body = '''Hi {first_name},

Thanks for registering to offer additional help through H2OFlint!

You can log back into the site any time to update your information by using {email} as your username and the password you created when you registered.

Thanks for using our site!

- H20Flint
'''


admin_add_help_email_subject = "We've received an offer for more individual help from {first_name} {last_name}."
admin_add_help_email_body = '''
We just received an individual helper registration for {first_name} {last_name}

Their info is:
------------------
email: {email}
Address: {address}, {city}, {state} {zipcode}
Phone: {phone}

Type of help:
Volunteer: {wants_to_volunteer}
Donate: {donated}
Park and serve: {wants_to_parkandserve}

'''