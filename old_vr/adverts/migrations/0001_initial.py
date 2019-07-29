# Generated by Django 2.2.3 on 2019-07-29 10:58

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('vehicle_type', models.CharField(choices=[('Car', 'Car'), ('Motor', 'Motor'), ('Other', 'Other')], max_length=100, verbose_name='Type')),
                ('vehicle_brand', models.CharField(max_length=100, verbose_name='Brand')),
                ('vehicle_model', models.CharField(max_length=100, verbose_name='Model')),
                ('city', models.CharField(max_length=100)),
                ('price_per_day', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Price/day')),
                ('available_from', models.DateField()),
                ('available_to', models.DateField()),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order_from', models.DateField(default=datetime.date.today)),
                ('order_to', models.DateField()),
                ('comment', models.TextField()),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='adverts.Advert')),
            ],
        ),
    ]