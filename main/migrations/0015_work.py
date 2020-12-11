# Generated by Django 3.1.4 on 2020-12-11 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20201211_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_title', models.CharField(blank=True, max_length=256, null=True)),
                ('work_title_en', models.CharField(blank=True, max_length=256, null=True)),
                ('work_title_ru', models.CharField(blank=True, max_length=256, null=True)),
                ('work_title_uz', models.CharField(blank=True, max_length=256, null=True)),
                ('btn_all', models.CharField(blank=True, max_length=256, null=True)),
                ('btn_all_en', models.CharField(blank=True, max_length=256, null=True)),
                ('btn_all_ru', models.CharField(blank=True, max_length=256, null=True)),
                ('btn_all_uz', models.CharField(blank=True, max_length=256, null=True)),
                ('btn_backend', models.CharField(blank=True, max_length=256, null=True)),
                ('btn_backend_en', models.CharField(blank=True, max_length=256, null=True)),
                ('btn_backend_ru', models.CharField(blank=True, max_length=256, null=True)),
                ('btn_backend_uz', models.CharField(blank=True, max_length=256, null=True)),
                ('btn_brand', models.CharField(blank=True, max_length=256, null=True)),
                ('btn_brand_en', models.CharField(blank=True, max_length=256, null=True)),
                ('btn_brand_ru', models.CharField(blank=True, max_length=256, null=True)),
                ('btn_brand_uz', models.CharField(blank=True, max_length=256, null=True)),
                ('btn_market', models.CharField(blank=True, max_length=256, null=True)),
                ('btn_market_en', models.CharField(blank=True, max_length=256, null=True)),
                ('btn_market_ru', models.CharField(blank=True, max_length=256, null=True)),
                ('btn_market_uz', models.CharField(blank=True, max_length=256, null=True)),
                ('img1', models.FileField(blank=True, null=True, upload_to='')),
                ('img2', models.FileField(blank=True, null=True, upload_to='')),
                ('img3', models.FileField(blank=True, null=True, upload_to='')),
                ('img4', models.FileField(blank=True, null=True, upload_to='')),
                ('img5', models.FileField(blank=True, null=True, upload_to='')),
                ('img6', models.FileField(blank=True, null=True, upload_to='')),
                ('num1', models.IntegerField(blank=True, null=True)),
                ('num2', models.IntegerField(blank=True, null=True)),
                ('num3', models.IntegerField(blank=True, null=True)),
                ('num4', models.IntegerField(blank=True, null=True)),
                ('comment1', models.CharField(blank=True, max_length=256, null=True)),
                ('comment1_en', models.CharField(blank=True, max_length=256, null=True)),
                ('comment1_ru', models.CharField(blank=True, max_length=256, null=True)),
                ('comment1_uz', models.CharField(blank=True, max_length=256, null=True)),
                ('comment2', models.CharField(blank=True, max_length=256, null=True)),
                ('comment2_en', models.CharField(blank=True, max_length=256, null=True)),
                ('comment2_ru', models.CharField(blank=True, max_length=256, null=True)),
                ('comment2_uz', models.CharField(blank=True, max_length=256, null=True)),
                ('comment3', models.CharField(blank=True, max_length=256, null=True)),
                ('comment3_en', models.CharField(blank=True, max_length=256, null=True)),
                ('comment3_ru', models.CharField(blank=True, max_length=256, null=True)),
                ('comment3_uz', models.CharField(blank=True, max_length=256, null=True)),
                ('comment4', models.CharField(blank=True, max_length=256, null=True)),
                ('comment4_en', models.CharField(blank=True, max_length=256, null=True)),
                ('comment4_ru', models.CharField(blank=True, max_length=256, null=True)),
                ('comment4_uz', models.CharField(blank=True, max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Work Item',
                'verbose_name_plural': 'Work Items',
            },
        ),
    ]
