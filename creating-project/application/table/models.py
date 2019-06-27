from django.db import models
from app.settings import BASE_DIR

# Create your models here.

class TableField(models.Model):
    position = models.IntegerField(verbose_name='порядковый номер')
    name = models.CharField(max_length=15, verbose_name='название поля')
    width = models.IntegerField(verbose_name='ширина поля')

    class Meta:
        verbose_name = 'поле'
        verbose_name_plural = 'поля'

    def __str__(self):
        return self.name


class TableFile(models.Model):
    path = models.FilePathField(path=BASE_DIR, verbose_name='путь к файлу')

    def set_path(self, new_path):
        self.path = new_path
        self.save()

    def get_path(self):
        return self.path

    def __str__(self):
        return str(self.path)

    class Meta:
        verbose_name = 'файл'
        verbose_name_plural = 'файлы'