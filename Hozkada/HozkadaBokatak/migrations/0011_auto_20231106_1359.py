# Generated by Django 3.1.4 on 2023-11-06 12:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HozkadaBokatak', '0010_auto_20231106_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eskaera',
            name='eskaera_data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
