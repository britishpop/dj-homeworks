from shop import views
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'), # домашняя страница
    path('signup/', views.shop_signup, name='signup'), # регистрация
    path('login/', views.shop_login, name='login'), # аутентификация
    path('logout/', views.ShopLogoutView.as_view(), name='logout'), # выход
    path('clothes/', views.ClothesListView.as_view(), name='clothes_cat'), # просмотр категории одежда. На всякий случай
    path('smartphones/', views.SmartphonesListView.as_view(), name='smartphones_cat'), # просмотр категории смартфонов
    path('empty/', views.empty, name='empty'), # пустая категория
    path('item/<int:pk>/', views.show_item, name='item'), # посмотреть отдельный телефон
    path('cart/', views.cart, name='cart'), # корзина
    path('order/', views.create_order, name='order'), # создание заказа
]