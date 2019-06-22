import time
import random

from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'

    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    search_term = request.GET['term']
    cached_value = cache.get(search_term)
    
    if not cached_value:
        response = City.objects.filter(name__icontains=search_term)
            # SQLite не умеет делать case-insensitive сравнение для Unicode
        results = []
        for city in response:
            results.append(city.name)
            cache.set(search_term, results, 600)
    else:
        results = cached_value

    return JsonResponse(results, safe=False)
