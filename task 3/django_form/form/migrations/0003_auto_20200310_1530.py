# Generated by Django 3.0.4 on 2020-03-10 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20200310_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infostore',
            name='phone',
            field=models.IntegerField(max_length=11),
        ),
    ]
