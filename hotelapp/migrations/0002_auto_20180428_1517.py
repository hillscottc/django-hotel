# Generated by Django 2.0.4 on 2018-04-28 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_res',
            field=models.DateField(verbose_name='Date of the stay.'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]