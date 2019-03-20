from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    landing_param = request.GET.get('from-landing')
    counter_click[landing_param] += 1
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    return render_to_response('index.html')


def landing(request):
    ab_test_arg = request.GET.get('ab-test-arg')  
    
    if ab_test_arg == 'original':
        counter_show[ab_test_arg] += 1
        return render_to_response('landing.html')
        
    elif ab_test_arg == 'test':
        counter_show[ab_test_arg] += 1
        return render_to_response('landing_alternate.html')
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    return render_to_response('landing.html')


def stats(request):
    print(counter_show)
    print(counter_click)
    if counter_show['test'] > 0:
        test_conversion = counter_click['test'] / counter_show['test']
    else:
        test_conversion = 0

    if counter_show['original'] > 0:
        original_conversion = counter_click['original'] / counter_show['original']
    else:
        original_conversion = 0
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
