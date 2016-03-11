# h2oflint
Code for www.h2oflint.com


**Setup and deployment tips**

1. To serve admin static files on Django in an Apache2 environment, do something like this:

First add this to your server config in /etc/apache2/sites-available/000-default.conf:
    Alias /static/admin/ "/home/ubuntu/h2oflint/venv/lib/python2.7/site-packages/django/contrib/admin/static"

Then run this symlink command:
    sudo ln -s /home/ubuntu/h2oflint/venv/lib/python2.7/site-packages/django/contrib/admin/static/admin /home/ubuntu/h2oflint/app/static


2. Create a Postgres database called h2oflint, with user flint and password 'waterisahumanright'


