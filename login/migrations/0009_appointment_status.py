# Generated by Django 2.2.6 on 2019-10-23 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20191023_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='unconfirmed', max_length=32),
        ),
    ]
