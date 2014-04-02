# Copyright

This directory contains a snapshot of code extracted from the following online tutorial:

https://docs.djangoproject.com/en/1.3/intro/

© 2005-2014 Django Software Foundation unless otherwise noted.

In fact, a simple RESTful API was added.

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

You can try out the fresh app by selecting the URL below the reload button.

http://rlaemmel.pythonanywhere.com/

## Prepare database

* Edit "/home/rlaemmel/mysite/settings.py" to select the sqlite DBMS.
* Open a bash console.
* From with the "mysite" dir, run "python manage.py syncdb".
* Confirm to create a superuser and enter login and password details.

## Fill in code of app

You can skip all "edit" and "create" steps for files and directories, if you just clone this github project. You still need to run the steps to sync the DB. Also, do not forget to reload the web app in the dashboard whenever you change files that are not reloaded automatically.

* From within the "mysite" dir, run "python manage.py startapp polls" to prepare app.
* Edit "mysite/polls/models.py" to define the model.
* Edit "mysite/settings.py" to install the polls and admin apps.
* From within the "mysite" dir, run "python manage.py syncdb" to add polls tables.
* From within the "mysite" dir, run "python manage.py sql polls" to have a look at polls tables.
* From within the "mysite" dir, run "python manage.py shell" to play with the polls API.
* Edit "mysite/urls.py" to activate the admin and to register various views of the polls app.
* Create file "mysite/polls/admin.py" to register poll app with admin.
* Create directory "mysite/templates" to hold templates.
* Edit "mysite/settings.py" to adjust TEMPLATE_DIRS.
* Edit "mysite/polls/views.py" to implement various views.
* Add "mysite/templates/polls/index.html".
* Add "mysite/templates/polls/detail.html".
* Add "mysite/templates/polls/results.html".

Steps for creating the RESTful API are left out here.

## Customize base-site template

These steps are optional. (They show additional means of customization.)

* Create and run "mysite/find.py" to locate Django installation.
* Copy Django's "contrib/admin/templates/admin/base_site.html" to the "templates/admin" dir.
* Edit "templates/admin/base_site.html" to customize it for the Polls app.

## The RESTful API

Additional files:
* mysite/polls/api.py
* mysite/polls/middleware.py

Affected files:
* mysite/settings.py (to disable CSRF)
* mysite/urls.py (to route URLs to API)

Illustrative client:
* https://github.com/rlaemmel/startup14/tree/master/rest_bot
