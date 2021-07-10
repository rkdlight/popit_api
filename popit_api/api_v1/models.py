from django.db import models
from django.contrib.postgres.fields import *
from datetime import date

from django.db.models.fields.related import ForeignKey

# Create your models here.

class User(models.Model):

    vk_id = models.CharField(verbose_name="VK ID", db_index=True, max_length=12)
    full_name = models.CharField(verbose_name="Полное имя", max_length=128)
    date_of_birth = models.DateField(verbose_name="Дата рождения", default = date(1900,1,1))
    friends = ArrayField(models.CharField(max_length=12), blank=True, null=True)
    coins_available = models.FloatField(verbose_name="Монеты", default=0)
    score = models.FloatField(verbose_name="Счёт", default=0)
    # make default value and SET_DRFAULT
    active_toy = models.ForeignKey('Toy', on_delete=models.SET_NULL, verbose_name="Текущая игрушка", null=True, blank=True)
    coins_by_sec = models.FloatField(verbose_name="Монет/сек", default=0.001)
    coins_by_click = models.FloatField(verbose_name="Монет/клик", default=0.001)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    last_date = models.DateTimeField(auto_now=True, verbose_name="Дата последней активности")
    refer = ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)
    buyed_updates = models.JSONField(verbose_name="Купленные улучшения", default=list)
    buyed_toys = models.JSONField(verbose_name="Купленные игрушки", default=list)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Toy(models.Model):

    name = models.CharField(max_length=128, verbose_name="Название")
    image = models.FileField(verbose_name="Изображение",blank=True)
    coins_by_click = models.FloatField(verbose_name="Монет/клик")
    pop_count = models.IntegerField(verbose_name="Количество пупырок")
    flipings_before_ad = models.IntegerField(verbose_name="Количество переворачиваний до рекламы")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Игрушка"
        verbose_name_plural = "Игрушки"

class Update(models.Model):

    name = models.CharField(max_length=128, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.FilePathField(verbose_name="Изображение",blank=True)
    coins_by_sec = models.FloatField(verbose_name="Монет/сек")
