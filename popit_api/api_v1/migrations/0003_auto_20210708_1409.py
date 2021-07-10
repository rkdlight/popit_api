# Generated by Django 3.2.5 on 2021-07-08 14:09

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0002_auto_20210708_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='buyed_toys',
            field=models.JSONField(blank=True, null=True, verbose_name='Купленные игрушки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='buyed_updates',
            field=models.JSONField(blank=True, null=True, verbose_name='Купленные улучшения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=12), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='refer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_v1.user'),
        ),
    ]