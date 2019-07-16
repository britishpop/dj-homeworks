from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.views.generic.list import ListView
from django.core.paginator import Paginator
from .models import Item, Review, Order, Shipping, ShopUser
from .forms import ReviewForm, ShopAuthForm, ShopUserCreationForm


# Create your views here.

def index(request):
    smartphones = Item.objects.filter(category__name__exact='smartphones')[:3] # взять последние три объекта
    clothes = Item.objects.filter(category__name__exact='clothes')[:3]

    context = {
        'smartphones': smartphones,
        'clothes': clothes,
    }

    return render(request, 'shop/index.html', context)

@login_required
def cart(request):
    if not request.session.session_key: # если нет сессии - создать ее
        request.session.save()

    if not request.session.get('cart_contents'): # если нет корзины в сессии - создать ее
        request.session['cart_contents'] = {}

    cart_contents = request.session['cart_contents']

    if request.method == 'POST': # запрос приходит после нажатия кнопки "Добавить в корзину"
        item_id = request.POST['item_id'] # смотрим какой товар пользователь добавил через кнопку
        if not cart_contents.get(item_id): # если этого товара еще не было в корзине - его кол-во станет 1
            cart_contents[item_id] = 1
        else:
            cart_contents[item_id] += 1 # если товар в корзине уже лежал - увеличить на 1
        request.session.modified = True # сохранить корзину в сессии

    object_list = [] # этот список товаров уйдет на рендер
    cart_count = 0 # отдельная переменная для подсчета кол-ва предметов в корзине

    for item in cart_contents:
        item_object = Item.objects.get(pk=item) # получим из базы объект товара
        quantity = cart_contents[item] # получим количество из корзины
        cart_count += int(quantity) # увеличим общий счетчик товаров в корзине
        object_list.append([item_object, quantity]) # добавим товар и количество в список на рендер

    context = {
        'cart_contents': object_list,
        'cart_count': cart_count,
    }

    return render(request, 'shop/cart.html', context)

@login_required
def create_order(request):
    if request.method == "POST":
        user = ShopUser.objects.get(pk=request.session['_auth_user_id']) # получить текущего юзера
        order = Order(pub_date=timezone.now(),user=user) # создать заказ
        order.save() # сохранить заказ, чтобы получить доступ к ManyToMany

        cart_contents = request.session['cart_contents'] # получить корзину
        for item in cart_contents:
            item_object = Item.objects.get(pk=item) # конкретный товар из корзины
            quantity = cart_contents[item] # количество товара
            shipping = Shipping(
                order=order,
                item=item_object,
                quantity=quantity
            )
            shipping.save() # создать through связь и записать туда количество
        request.session['cart_contents'] = {} # опустошить корзину после создания товара
        request.session.modified = True # записать сессию

        return render(request, 'shop/order_success.html', {'id': order.id})

    else:
        return redirect('shop:index')

def empty(request):
    return render(request, 'shop/empty_section.html')


def shop_signup(request):
    if request.method == 'POST':
        form = ShopUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(False)
            new_user.username = new_user.email
            new_user.save()
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
            return redirect('shop:index')
    else:
        form = ShopUserCreationForm()

    return render(
        request,
        'account/signup.html',
        {'form': form}
    )


def shop_login(request):
    form = ShopAuthForm()

    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if request.GET.get('next') and 'cart' in request.GET.get('next'):
                return redirect('shop:cart')
            return redirect('shop:index')

    return render(
        request,
        'account/login.html',
        {'form': form}
    )


def show_item(request, pk):
    phone = Item.objects.get(pk=pk)
    form = ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        form.is_valid()
        data = form.cleaned_data
        review = Review(author=data['author'], text=data['text'], rating=int(data['rating']),item=phone)
        review.save()

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
        try:
            current_page = int(self.request.GET.get('page', 1))
        except ValueError:
            current_page = 1
        
        all_items = Item.objects.filter(category__name__exact='smartphones')
        paginated_items = Paginator(all_items, 3)
        queryset = paginated_items.get_page(current_page)
        
        return queryset


class ClothesListView(ListView):
    template_name = 'shop/smartphones.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        try:
            current_page = int(self.request.GET.get('page', 3))
        except ValueError:
            current_page = 1
        
        all_items = Item.objects.filter(category__name__exact='clothes')
        paginated_items = Paginator(all_items, 10)
        queryset = paginated_items.get_page(current_page)
        
        return queryset