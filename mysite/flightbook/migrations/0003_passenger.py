# Generated by Django 2.1 on 2018-08-24 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightbook', '0002_flighttypes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=20)),
                ('source', models.CharField(max_length=20)),
                ('dest', models.CharField(max_length=20)),
                ('seats', models.CharField(max_length=1)),
                ('date', models.CharField(max_length=10)),
                ('code', models.CharField(max_length=6)),
                ('flight_name', models.CharField(max_length=20)),
                ('dept_time', models.CharField(max_length=10)),
                ('arrival_time', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
                ('duration', models.CharField(max_length=10)),
            ],
            options={
                'get_latest_by': 'id',
            },
        ),
    ]