# Generated by Django 4.2.11 on 2024-05-06 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motel_meo', '0003_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
