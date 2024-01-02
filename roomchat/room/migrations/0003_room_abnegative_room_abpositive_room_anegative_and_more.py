# Generated by Django 5.0 on 2024-01-01 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_room_maps_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='ABnegative',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='ABpositive',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='Anegative',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='Apositive',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='Bnegative',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='Bpositive',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='Onegative',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='Opositive',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
