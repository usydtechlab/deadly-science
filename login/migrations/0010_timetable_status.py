# Generated by Django 2.2.6 on 2019-10-24 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='status',
            field=models.CharField(default='available', max_length=32),
        ),
    ]
