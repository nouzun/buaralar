from django.shortcuts import get_object_or_404, render

from posts.models import Event


def index(request):
    latest_event_list = Event.objects.order_by('-pub_date')[:5]
    context = {'latest_event_list': latest_event_list}
    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    event = get_object_or_404(Event, pk=post_id)
    return render(request, 'posts/detail.html', {'event': event})