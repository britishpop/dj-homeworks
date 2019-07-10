from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms.widgets import PasswordInput, TextInput, Textarea
from .models import ShopUser


# форма использовалась для логина по юзернейму
# class ShopAuthForm(AuthenticationForm): 
#     username = forms.CharField(widget=TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Электронный адрес',}
#     ))
#     password = forms.CharField(widget=PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder':'Пароль',}
#     ))


class ShopUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = ShopUser
        fields = ('username', 'email')

    
class ShopUserChangeForm(UserChangeForm):

    class Meta:
        model = ShopUser
        fields = ('username', 'email')


class ReviewForm(forms.Form):
    author = forms.CharField(label='Имя', widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Представьтесь'},
    ))
    text = forms.CharField(label='Расскажите впечатления', widget=Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Ваш отзыв',}
    ))
    rating = forms.ChoiceField(label='Поставьте оценку', widget=forms.RadioSelect(attrs={
        'class': 'form-check-input position-relative',}
        ),
        choices=[
        ('1', 'Плохо'),
        ('2', 'Ну такое'),
        ('3', 'Средне'),
        ('4', 'Хорошо'),
        ('5', 'Ваще норм'),
    ])