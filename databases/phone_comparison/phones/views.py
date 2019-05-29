from django.shortcuts import render
from phones.models import Chinaphone, Iphone

def show_catalog(request):
    phones = []

    iphones = Iphone.objects.all()
    chinaphones = Chinaphone.objects.all()

    for phone in iphones:
        phones.append(phone)
    
    for phone in chinaphones:
        phones.append(phone)

    return render(
        request,
        'catalog.html',
        {'phones': phones}
    )
