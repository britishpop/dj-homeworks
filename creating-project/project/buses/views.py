from django.shortcuts import render, get_object_or_404
from .models import Station, Route
from django.db.models import Avg

# Create your views here.


def bus_display(request):
    routes = Route.objects.all()
    context = {'routes': routes,}

    if request.GET.get('route'):
        current_route = get_object_or_404(Route, name=request.GET.get('route'))
        stations = current_route.stations.all()
        context['stations'] = stations
        context['center'] = {
            'x': stations.aggregate(Avg('longitude'))['longitude__avg'],
            'y': stations.aggregate(Avg('latitude'))['latitude__avg'],
        }

    return render(
        request,
        'stations.html',
        context
    )