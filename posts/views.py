import datetime
from django.shortcuts import get_object_or_404, render

from posts.models import Event


def index(request):
    latest_event_list = Event.objects.order_by('-pub_date')[:5]
    selected_event = latest_event_list[0]
    third_day = (datetime.date.today() + datetime.timedelta(days=2)).strftime("%A").lower()
    this_year = datetime.date.today().year
    context = {'latest_event_list': latest_event_list, 'third_day': third_day, 'this_year': this_year, 'selected_event': selected_event}
    return render(request, 'posts/index.html', context)


def get_selected_event(request, post_id):
    latest_event_list = Event.objects.order_by('-pub_date')[:5]
    selected_event = Event.objects.get(id=post_id)
    third_day = (datetime.date.today() + datetime.timedelta(days=2)).strftime("%A").lower()
    this_year = datetime.date.today().year
    context = {'latest_event_list': latest_event_list, 'third_day': third_day, 'this_year': this_year, 'selected_event': selected_event}
    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    event = get_object_or_404(Event, pk=post_id)
    return render(request, 'posts/detail.html', {'event': event})