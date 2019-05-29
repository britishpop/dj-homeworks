from django.db import models

# Create your models here.

class Phone(models.Model):
    phone_name = models.CharField(verbose_name='Модель', max_length=50)
    phone_type = models.CharField(verbose_name='Тип', max_length=10)
    phone_form = models.CharField(verbose_name='Форм-фактор', max_length=15)
    gsm_900_1800 = models.BooleanField(verbose_name='GSM 900/1800', max_length=10)
    gsm_1900 = models.BooleanField(verbose_name='GSM 1900', max_length=10)
    gsm_3g = models.BooleanField(verbose_name='3G', max_length=10)
    sim_type = models.CharField(verbose_name='Тип SIM', max_length=10)
    OS = models.CharField(verbose_name='ОС', max_length=10)

    def __str__(self):
        return self.phone_name

    class Meta:
        abstract = True
    
class Chinaphone(Phone):
    mem_card = models.CharField(verbose_name='Карта памяти', max_length=10)
    radio = models.BooleanField(verbose_name='FM-модуль', max_length=10)
    sim_quantity = models.IntegerField(verbose_name='Количество SIM')

class Iphone(Phone):
    animoji = models.BooleanField(verbose_name='Поддержка Animoji', max_length=10)
    imessage = models.BooleanField(verbose_name='Поддержка iMessage', max_length=10)