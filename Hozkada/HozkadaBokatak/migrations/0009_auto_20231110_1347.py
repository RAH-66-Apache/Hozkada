# Generated by Django 3.1.4 on 2023-11-10 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HozkadaBokatak', '0008_alter_alergia_id_alter_alergia_platerra_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bezeroa',
            old_name='NAN',
            new_name='nan',
        ),
        migrations.AddField(
            model_name='platerra',
            name='deskontua',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='alergia',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='alergia_platerra',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bezeroa',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='deskontua',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='deskontua_platerra',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='eskaera',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='platerra',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='platerra_eskaera',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
