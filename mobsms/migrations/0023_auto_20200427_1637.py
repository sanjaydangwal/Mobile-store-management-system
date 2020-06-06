# Generated by Django 3.0.5 on 2020-04-27 11:07

from django.db import migrations, models
import mobsms.models


class Migration(migrations.Migration):

    dependencies = [
        ('mobsms', '0022_auto_20200424_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic',
            name='Battery_capacity',
            field=models.IntegerField(validators=[mobsms.models.validatePositive]),
        ),
        migrations.AlterField(
            model_name='basic',
            name='Internal_storage',
            field=models.IntegerField(validators=[mobsms.models.validatePositive]),
        ),
        migrations.AlterField(
            model_name='basic',
            name='Ram',
            field=models.IntegerField(blank=True, null=True, validators=[mobsms.models.validatePositive]),
        ),
        migrations.AlterField(
            model_name='phone',
            name='Price',
            field=models.IntegerField(validators=[mobsms.models.validatePositive]),
        ),
        migrations.AlterField(
            model_name='phone',
            name='Quantity',
            field=models.IntegerField(default=1, validators=[mobsms.models.validatePositive]),
        ),
        migrations.AlterField(
            model_name='smart',
            name='Battery_capacity',
            field=models.IntegerField(validators=[mobsms.models.validatePositive]),
        ),
        migrations.AlterField(
            model_name='smart',
            name='Expandable_storage',
            field=models.SmallIntegerField(blank=True, null=True, validators=[mobsms.models.validatePositive]),
        ),
        migrations.AlterField(
            model_name='smart',
            name='Internal_storage',
            field=models.IntegerField(validators=[mobsms.models.validatePositive]),
        ),
        migrations.AlterField(
            model_name='smart',
            name='Ram',
            field=models.IntegerField(validators=[mobsms.models.validatePositive]),
        ),
        migrations.AlterField(
            model_name='smart',
            name='Weight',
            field=models.IntegerField(blank=True, null=True, validators=[mobsms.models.validatePositive]),
        ),
    ]