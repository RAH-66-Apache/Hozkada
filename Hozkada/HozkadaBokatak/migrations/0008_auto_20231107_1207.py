# Generated by Django 3.1.4 on 2023-11-07 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HozkadaBokatak', '0007_bezeroa_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bezeroa',
            name='img',
            field=models.ImageField(default='img/erabiltzaileak/logo.png', upload_to='img/erabiltzaileak'),
        ),
    ]
