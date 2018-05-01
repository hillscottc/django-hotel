# Generated by Django 2.0.4 on 2018-05-01 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180430_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='client_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_end',
            field=models.DateField(default='2020-01-07', verbose_name='End of the stay.'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_start',
            field=models.DateField(default='2020-01-01', verbose_name='Start of the stay.'),
        ),
    ]