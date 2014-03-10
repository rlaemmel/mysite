# Copyright

This directory contains a snapshot of code extracted from the following online tutorial:
https://docs.djangoproject.com/en/1.3/intro/
© 2005-2014 Django Software Foundation unless otherwise noted.

# Objective

The content has been assembled by Ralf Lämmel, http://softlang.wikidot.com/
The idea is to capture all the steps needed for reproducing the "first Django app" at pythonanywhere.com.
If you want to reproduce, replace "rlaemmel" in the following steps by your "user" at pythonanywhere.com.

# Steps

## Create web app

Lets assume we are looking at a virgin pythonanywhere account.

* Go to the "Dashboard".
* Select "Web".
* Click "Add a new web app" to actually create a project.
* Select the "rlaemmel.pythonanywhere.com" domain.
* Select "Django".
* Select "Python 2.7 (Django 1.3.7)".

## Try out fresh app

* Select the web app URL below the reload button.
* That is, browse to "http://rlaemmel.pythonanywhere.com/".

## Prepare database

* Edit "/home/rlaemmel/mysite/settings.py" to select the sqlite DBMS.
* Open a bash console.
* From with the "mysite" dir, run "python manage.py syncdb".
* Confirm to create a superuser and enter such details.

## Fill in code of app

* From with the “mysite” dir, run “python manage.py startapp polls” to prepare app.
* Edit “mysite/polls/models.py” to define the model.
* Edit “mysite/settings.py” to install the polls and admin apps.
* From with the “mysite” dir, run “python manage.py syncdb” to add polls tables.
* From with the “mysite” dir, run “python manage.py sql polls” to have a look at polls tables.
* From with the “mysite” dir, run “python manage.py shell” to play with the polls API.
* Edit “mysite/urls.py” to activate the admin site.
* Create file “mysite/polls/admin.py” to register poll app with admin.
* Create directory “mysite/templates” to hold templates.
* Edit “mysite/settings.py” to adjust TEMPLATE_DIRS.
* Edit “mysite/urls.py” to active various views.
* Edit “mysite/polls/views.py” to implement various views.
* Add “mysite/templates/polls/index.html”.
* Add “mysite/templates/polls/detail.html”.
* Add “mysite/templates/polls/results.html”.

## Customize base-site template

These steps are optional.

* Create and run “mysite/find.py” to locate Django installation.
* Copy Django's “contrib/admin/templates/admin/base_site.html” to the “templates/admin” dir.
* Edit “templates/admin/base_site.html” to customize it for the Polls app.
