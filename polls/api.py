# A very simple RESTful API

from mysite.polls.models import Poll, Choice
from django import http
from django.utils import simplejson as json
from django.shortcuts import get_object_or_404
from django.http import Http404

# Return all polls in JSON
def index(request):
    poll_list = Poll.objects.all()
    poll_dict = dict()
    for p in poll_list:
        poll_dict[p.id] = p.question
    content = json.dumps(poll_dict)
    return http.HttpResponse(content,
                content_type='application/json')

# Return choices with numbers of votes for a poll in JSON
def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    choice_dict = dict()
    for c in p.choice_set.all():
        choice_dict[c.id] = dict()
        choice_dict[c.id]["choice"] = c.choice
        choice_dict[c.id]["votes"] = c.votes
    content = json.dumps(choice_dict)
    return http.HttpResponse(content,
                content_type='application/json')

# Count a vote towards a choice of a poll; return votes count in JSON
def vote(request):
    dict_content = json.loads(request.raw_post_data)
    poll_id = int(dict_content['poll'])
    choice_id = int(dict_content['choice'])
    try:
        p = Poll.objects.get(pk=poll_id)
        c = p.choice_set.get(pk=choice_id)
    except (KeyError, Choice.DoesNotExist):
        raise Http404()
    c.votes += 1
    c.save()
    return http.HttpResponse(json.dumps(c.votes),
        content_type='application/json')
