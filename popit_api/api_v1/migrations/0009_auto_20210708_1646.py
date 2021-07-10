# Generated by Django 3.2.5 on 2021-07-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0008_auto_20210708_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='buyed_toys',
            field=models.JSONField(default='dict', verbose_name='Купленные игрушки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='buyed_updates',
            field=models.JSONField(default='dict', verbose_name='Купленные улучшения'),
        ),
    ]
