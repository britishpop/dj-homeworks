from django.shortcuts import render
from .models import Station, Route
from django.db.models import Avg

# Create your views here.


def bus_display(request):
    routes = Route.objects.all()
    context = {'routes': routes, 'center': CENTER,}

    if request.GET.get('route'):
        current_route = Route.objects.get(name=request.GET.get('route'))
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