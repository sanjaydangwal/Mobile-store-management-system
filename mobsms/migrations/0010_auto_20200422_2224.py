# Generated by Django 3.0.5 on 2020-04-22 16:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mobsms', '0009_auto_20200422_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
