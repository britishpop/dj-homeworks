# Generated by Django 2.1.7 on 2019-05-30 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(verbose_name='Наличие LTE'),
        ),
    ]
