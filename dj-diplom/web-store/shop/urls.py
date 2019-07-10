from shop import views
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'), # домашняя страница
    path('clothes/', views.ClothesListView.as_view(), name='clothes_cat'), # просмотр категории одежда. На всякий случай
    path('smartphones/', views.SmartphonesListView.as_view(), name='smartphones_cat'), # просмотр категории смартфонов
    path('empty/', views.empty, name='empty'), # пустая категория
    path('item/<int:pk>/', views.show_item, name='item'), # посмотреть отдельный телефон
    path('cart/', views.cart, name='cart'), # корзина
    path('order/', views.create_order, name='order'), # создание заказа
    path('logout/', views.ShopLogoutView.as_view(), name='logout'), # выход через свою вьюху

    # path('signup/', views.shop_signup, name='signup'), # регистрация через свою вьюху по юзернейму
    # path('login/', views.shop_login, name='login'), # аутентификация через свою вьюху по юзернейму
]