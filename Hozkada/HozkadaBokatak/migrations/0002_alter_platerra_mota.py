# Generated by Django 4.2.5 on 2023-11-04 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HozkadaBokatak', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platerra',
            name='mota',
            field=models.CharField(choices=[('haragia', 'Haragia'), ('arraina', 'Arraina'), ('begetarianoa', 'Begetarianoa'), ('beganoa', 'Beganoa')], default='haragia', max_length=20),
        ),
    ]