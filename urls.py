from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #
    # An experiment with a RESTful API
    #
    url(r'^api/polls/$', 'mysite.polls.api.index'),
    url(r'^api/polls/(?P<poll_id>\d+)/$', 'mysite.polls.api.detail'),
    url(r'^api/vote/$', 'mysite.polls.api.vote'),
    #
    # What follows is from the basic webapp
    #
    url(r'^polls/$', 'mysite.polls.views.index'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'mysite.polls.views.detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$', 'mysite.polls.views.results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'mysite.polls.views.vote'),
    url(r'^admin/', include(admin.site.urls)),
)