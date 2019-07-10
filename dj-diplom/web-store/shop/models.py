from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class ShopUser(AbstractUser):
    
    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField('категория', max_length=100)
        
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField('название', max_length=100)
    description = models.CharField('описание', max_length=250)
    img = models.FileField('изображение', upload_to='%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    
    def __str__(self):
        return '%s %s' % (self.category, self.name)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Review(models.Model):
    author = models.CharField('автор', max_length=100)
    text = models.TextField('текст')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'обзор'
        verbose_name_plural = 'обзоры'
    
    def __str__(self):
        return '%s %s ...' % (self.author, self.text[:10])


class Order(models.Model):
    pub_date = models.DateTimeField('дата создания')
    user = models.ForeignKey(ShopUser, on_delete=models.CASCADE, related_name='orders')
    items = models.ManyToManyField(Item, related_name='orders', through='Shipping')

    def items_count(self):
        count = 0
        for shipping in self.shipping_set.all():
            count += shipping.quantity
        return count

    def __str__(self):
        return 'Заказ %s пользователя %s' % (self.id, self.user)


class Shipping(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('количество', default=0)

    def __str__(self):
        return 'Продукт %s в заказе %s' % (self.item, self.order.id)
