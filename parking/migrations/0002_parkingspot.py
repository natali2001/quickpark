# Generated by Django 2.2.12 on 2023-03-02 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parking_type', models.CharField(choices=[('I', 'Indoor'), ('O', 'Outdoor')], max_length=1)),
                ('is_booked', models.BooleanField(default=False)),
            ],
        ),
    ]
