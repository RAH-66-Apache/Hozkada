# Generated by Django 3.1.4 on 2023-11-06 12:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HozkadaBokatak', '0009_auto_20231106_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eskaera',
            name='eskaera_data',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 6, 12, 59, 10, 654279, tzinfo=utc)),
        ),
    ]
