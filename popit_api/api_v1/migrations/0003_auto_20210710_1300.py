# Generated by Django 3.2.5 on 2021-07-10 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0002_auto_20210710_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='friends',
        ),
        migrations.AddField(
            model_name='user',
            name='friend',
            field=models.ManyToManyField(blank=True, related_name='friends', to='api_v1.User'),
        ),
    ]
