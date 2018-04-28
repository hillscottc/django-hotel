# Generated by Django 2.0.4 on 2018-04-28 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('res_buffer', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100)),
                ('date_res', models.DateTimeField(verbose_name='Date of the stay.')),
                ('date_updated', models.DateTimeField(verbose_name='Date res placed/updated.')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.Hotel')),
            ],
        ),
    ]