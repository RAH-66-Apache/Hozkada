# Generated by Django 3.1.4 on 2023-11-06 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HozkadaBokatak', '0006_auto_20231106_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eskaera',
            name='eskaera_data',
        ),
    ]
