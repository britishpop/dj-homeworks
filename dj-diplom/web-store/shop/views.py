from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import ListView
from django.contrib.auth.views import LogoutView
from .models import Item
from .forms import ShopAuthForm, ReviewForm

# Create your views here.

def index(request):
    smartphones = Item.objects.filter(category__name__exact='smartphones')[:3]
    clothes = Item.objects.filter(category__name__exact='clothes')[:3]

    context = {
        'smartphones': smartphones,
        'clothes': clothes,
    }

    return render(request, 'shop/index.html', context)

def cart(request):
    return render(request, 'shop/cart.html')

def empty(request):
    return render(request, 'shop/empty_section.html')

def shop_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:index')
    else:
        form = UserCreationForm()

    return render(
        request,
        'shop/signup.html',
        {'form': form}
    )


def shop_login(request):
    form = ShopAuthForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop:index')

    return render(
        request,
        'shop/login.html',
        {'form': form}
    )


def show_item(request, pk):
    phone = Item.objects.get(pk=pk) # TODO: prefetch related
    form = ReviewForm()
    
    if request.method == 'POST':
        print('hey') # TODO: post review

    context = {
        'object': phone,
        'form': form,
    }

    return render(request, 'shop/phone.html', context)


class ShopLogoutView(LogoutView):
    pass


class SmartphonesListView(ListView):
    template_name = 'shop/smartphones.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.filter(category__name__exact='smartphones')


class ClothesListView(ListView):
    template_name = 'shop/smartphones.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.filter(category__name__exact='clothes')