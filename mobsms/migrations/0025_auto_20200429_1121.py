# Generated by Django 3.0.5 on 2020-04-29 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobsms', '0024_basic_expandable_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pic/default.png', upload_to='profile_pic'),
        ),
    ]
