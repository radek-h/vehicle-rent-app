# Generated by Django 2.2.3 on 2019-07-30 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0005_auto_20190730_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='availability',
        ),
    ]