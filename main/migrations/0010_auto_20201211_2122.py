# Generated by Django 3.1.4 on 2020-12-11 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='service_info',
            new_name='backend_info',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_info_en',
            new_name='backend_info_en',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_info_ru',
            new_name='backend_info_ru',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_info_uz',
            new_name='backend_info_uz',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_title',
            new_name='backend_title',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_title_en',
            new_name='backend_title_en',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_title_ru',
            new_name='backend_title_ru',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_title_uz',
            new_name='backend_title_uz',
        ),
        migrations.AddField(
            model_name='service',
            name='brand_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='brand_info_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='brand_info_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='brand_info_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='brand_title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='brand_title_en',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='brand_title_ru',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='brand_title_uz',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='consult_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='consult_info_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='consult_info_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='consult_info_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='consult_title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='consult_title_en',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='consult_title_ru',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='consult_title_uz',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='marketing_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='marketing_info_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='marketing_info_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='marketing_info_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='marketing_title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='marketing_title_en',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='marketing_title_ru',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='marketing_title_uz',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
