# Generated by Django 4.2.11 on 2024-04-29 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Motel-Meo', max_length=45)),
                ('location', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Hotels',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(choices=[('1', 'Single'), ('2', 'Double'), ('3', 'Suite'), ('4', 'Triple')], max_length=50)),
                ('status', models.CharField(choices=[('1', 'Available'), ('2', 'Not Available')], max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('capacity', models.PositiveIntegerField()),
                ('size', models.PositiveIntegerField()),
                ('room_no', models.PositiveIntegerField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motel_meo.hotel')),
            ],
            options={
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('booking_id', models.CharField(default='null', max_length=155)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motel_meo.room')),
            ],
            options={
                'verbose_name_plural': 'Booking',
            },
        ),
    ]