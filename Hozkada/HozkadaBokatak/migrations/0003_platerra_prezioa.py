# Generated by Django 4.2.5 on 2023-11-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HozkadaBokatak', '0002_alter_platerra_mota'),
    ]

    operations = [
        migrations.AddField(
            model_name='platerra',
            name='prezioa',
            field=models.FloatField(default=0),
        ),
    ]
