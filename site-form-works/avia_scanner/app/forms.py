import datetime
from django import forms
from bootstrap_datepicker_plus import DatePickerInput

from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    city_from = forms.CharField(
        label = 'Откуда',
        widget = AjaxInputWidget(
            'api/city_ajax',
            attrs = {
                'class': 'form-control'
            }
        )
    )
    city_to = forms.ChoiceField(
        label = 'Куда',
        choices = [(str(i), str(i)) for i in City.objects.all().order_by('name')],
        widget = forms.Select(
            attrs = {
                'class': 'form-control'
            }
        )
    )
    date = forms.DateField(
        label = 'Когда',
        widget = DatePickerInput(
            format = '%m/%d/%Y',
            options = {
                "showTodayButton": True,
            }
        )
    )



