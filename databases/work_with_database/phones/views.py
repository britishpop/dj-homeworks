from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from phones.models import Phone


def show_catalog(request):
    sort = request.GET.get('sort')

    if sort == 'name':
        phones = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()

    return render(
        request,
        'catalog.html',
        {'phones': phones}
    )


def show_product(request, slug):
    try:
        phone = Phone.objects.get(slug=slug)
        status = '200'
    except ObjectDoesNotExist:
        phone = 'Искомый телефон не найден'
        status = '404'
    
    return render(
        request,
        'product.html',
        {
            'status': status,
            'phone': phone
        }
    )
