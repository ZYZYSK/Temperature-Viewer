# Generated by Django 3.2.12 on 2022-03-10 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_daydata_humidity_max'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daydata',
            name='humidity_ave',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timedata',
            name='humidity',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
