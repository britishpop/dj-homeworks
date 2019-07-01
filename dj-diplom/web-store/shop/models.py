from django.db import models

# Create your models here.

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
