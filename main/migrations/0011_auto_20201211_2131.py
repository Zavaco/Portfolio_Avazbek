# Generated by Django 3.1.4 on 2020-12-11 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20201211_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='brand_logo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='service',
            name='consult_logo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='service',
            name='marketing_logo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
