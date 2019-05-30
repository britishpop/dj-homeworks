from django.db import models


class Phone(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(verbose_name='Название', max_length=100)
    price = models.IntegerField(verbose_name='Цена')
    image = models.CharField(verbose_name='Изображение', max_length=100)
    release_date = models.DateField(verbose_name='Дата выхода')
    lte_exists = models.BooleanField(verbose_name='Наличие LTE')
    slug = models.CharField(verbose_name='Ссылка', max_length=100)
    
    def __str__(self):
        return self.name
