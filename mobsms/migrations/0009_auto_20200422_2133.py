# Generated by Django 3.0.5 on 2020-04-22 16:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mobsms', '0008_checkout_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='Date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
