# Generated by Django 3.1.4 on 2020-12-11 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201211_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='phone_info_en',
        ),
        migrations.RemoveField(
            model_name='about',
            name='phone_info_ru',
        ),
        migrations.RemoveField(
            model_name='about',
            name='phone_info_uz',
        ),
    ]
