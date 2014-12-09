import datetime
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext

from posts.models import Event


def index(request):
    selected_event = None

    desiredDate = datetime.date.today()

    today_min = datetime.datetime.combine(desiredDate, datetime.time.min)
    today_max = datetime.datetime.combine(desiredDate, datetime.time.max)

    latest_event_list = Event.objects.filter(event_date_begin__range=(today_min, today_max)).order_by('-event_date_begin')[:6]

    latest_event_list = Event.objects.order_by('-pub_date')[:5]
    if len(latest_event_list) > 0:
        selected_event = latest_event_list[0]
    third_day = (datetime.date.today() + datetime.timedelta(days=2)).strftime("%A").lower()
    this_year = datetime.date.today().year
    context = {'latest_event_list': latest_event_list, 'third_day': third_day, 'this_year': this_year, 'selected_event': selected_event, 'selected_day': 'today'}
    return render(request, 'posts/index.html', context)

def posts_views_get_selected_day(request, day):
    selected_event = None
    desiredDate = datetime.date.today()
    if day == 'tomorrow':
        desiredDate = datetime.date.today() + datetime.timedelta(days=1)
    elif day == 'nextday':
        desiredDate = datetime.date.today() + datetime.timedelta(days=2)

    today_min = datetime.datetime.combine(desiredDate, datetime.time.min)
    today_max = datetime.datetime.combine(desiredDate, datetime.time.max)

    latest_event_list = Event.objects.filter(event_date_begin__range=(today_min, today_max)).order_by('-event_date_begin')[:6]
    if len(latest_event_list) > 0:
        selected_event = latest_event_list[0]
    third_day = (datetime.date.today() + datetime.timedelta(days=2)).strftime("%A").lower()
    this_year = datetime.date.today().year
    context = {'latest_event_list': latest_event_list, 'third_day': third_day, 'this_year': this_year, 'selected_event': selected_event, 'selected_day': day}
    return render(request, 'posts/index.html', context)

def posts_views_get_selected_event_ajax(request, post_id):
    context = RequestContext(request)
    selected_event = get_object_or_404(Event, pk=post_id)
    return render_to_response('posts/detail.html', {'selected_event': selected_event }, context)

def posts_views_get_selected_event(request, post_id):
    event_day = None
    selected_event = get_object_or_404(Event, pk=post_id)
    desiredDate = datetime.date.today()

    today_min = datetime.datetime.combine(desiredDate, datetime.time.min)
    today_max = datetime.datetime.combine(desiredDate, datetime.time.max)

    latest_event_list = Event.objects.filter(event_date_begin__range=(today_min, today_max)).order_by('-event_date_begin')[:6]
    third_day = (datetime.date.today() + datetime.timedelta(days=2)).strftime("%A").lower()
    this_year = datetime.date.today().year

    today = datetime.date.today()
    tomorrow = (datetime.date.today() + datetime.timedelta(days=1))
    third_day = (datetime.date.today() + datetime.timedelta(days=2))
    forth_day = (datetime.date.today() + datetime.timedelta(days=3))
    if (selected_event.event_date_begin.date() >= today) & (selected_event.event_date_begin.date() < tomorrow):
        event_day = 'today'
    elif (selected_event.event_date_begin.date() >= tomorrow) & (selected_event.event_date_begin.date() < third_day):
        event_day = 'tomorrow'
    elif (selected_event.event_date_begin.date() >= third_day) & (selected_event.event_date_begin.date() < forth_day):
        event_day = 'nextday'

    context = {'latest_event_list': latest_event_list, 'third_day': third_day, 'this_year': this_year, 'selected_event': selected_event, 'selected_day': event_day}
    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    event = get_object_or_404(Event, pk=post_id)
    return render(request, 'posts/detail.html', {'event': event})