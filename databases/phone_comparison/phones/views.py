from django.shortcuts import render
from django.views.generic.list import ListView
from phones.models import Phone

class PhoneList(ListView):
    model = Phone

    template_name = 'catalog.html'
    context_object_name = 'phones'

def show_catalog(request):
    context = []
    phones = Phone.objects.all()

    return render(
        request,
        'catalog.html',
        context
    )
