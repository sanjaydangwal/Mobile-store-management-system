# Generated by Django 3.0.5 on 2020-04-23 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobsms', '0013_auto_20200423_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smart',
            name='Primary_clock_speed',
            field=models.FloatField(),
        ),
    ]
