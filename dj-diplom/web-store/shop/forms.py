from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, Textarea


class ShopAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control','placeholder': 'Электронный адрес'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control','placeholder':'Пароль'}))


class ReviewForm(forms.Form):
    author = forms.CharField(label='Имя', widget=TextInput(attrs={'class': 'form-control','placeholder': 'Представьтесь'}))
    text = forms.CharField(label='Расскажите впечатления', widget=Textarea(attrs={'class': 'form-control','placeholder': 'Ваш отзыв'}))
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=[
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five'),
    ])