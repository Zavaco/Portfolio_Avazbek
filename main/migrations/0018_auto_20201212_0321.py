# Generated by Django 3.1.4 on 2020-12-11 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20201212_0228'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormCreate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.CharField(blank=True, max_length=256, null=True)),
                ('subject', models.CharField(blank=True, max_length=256, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Form Item',
                'verbose_name_plural': 'Form Items',
            },
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='message',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
    ]
