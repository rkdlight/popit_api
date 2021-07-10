# Generated by Django 3.2.5 on 2021-07-08 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0003_auto_20210708_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='active_toy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_v1.toy', verbose_name='Текущая игрушка'),
        ),
    ]
