# Generated by Django 3.0.5 on 2020-04-21 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobsms', '0002_auto_20200421_2154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='category',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='Model_Name',
            new_name='Model_name',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='Model_Number',
            new_name='Model_number',
        ),
    ]
