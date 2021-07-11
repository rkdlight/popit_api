from django.db import models
from django.contrib.postgres.fields import *
from datetime import date

# Create your models here.
class Toy(models.Model):
    
    name = models.CharField(max_length=128, verbose_name="Название")
    image = models.FileField(verbose_name="Изображение",blank=True)
    base_price = models.FloatField(verbose_name="Цена", default=0)
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
    base_price = models.FloatField(verbose_name="Цена", default=0)
    image = models.FilePathField(verbose_name="Изображение", blank=True)
    coins_by_sec = models.FloatField(verbose_name="Монет/сек")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Улучшение"
        verbose_name_plural = "Улучшения"

class User(models.Model):

    vk_id = models.IntegerField(verbose_name="VK ID", db_index=True, primary_key=True)
    full_name = models.CharField(verbose_name="Полное имя", max_length=128)
    date_of_birth = models.DateField(verbose_name="Дата рождения", default = date(1900,1,1))
    friend = models.ManyToManyField('User', blank=True, related_name="friends")
    coins_available = models.FloatField(verbose_name="Монеты", default=0)
    score = models.FloatField(verbose_name="Счёт", default=0)
    active_toy = models.ForeignKey('Toy', on_delete=models.SET_NULL, null=True, blank=True)
    coins_by_sec = models.FloatField(verbose_name="Монет/сек", default=0.001)
    coins_by_click = models.FloatField(verbose_name="Монет/клик", default=0.001)
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    last_date = models.DateTimeField(auto_now=True, verbose_name="Дата последней активности")
    refer = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True, related_name='referals')
    buyed_updates = models.JSONField(verbose_name="Купленные улучшения", default=list)
    '''
        [
            {"id": 1, "count":3, "current_price": 1.5},
            {"id": 4, "count":3, "current_price": 11.5},
            {"id": 5, "count":6, "current_price": 110.5},
        ]
    '''
    buyed_toys = models.JSONField(verbose_name="Купленные игрушки", default=list)
    '''
        [
            {"id": 1, "count":3, "current_price": 1.5},
            {"id": 4, "count":3, "current_price": 11.5},
            {"id": 5, "count":6, "current_price": 110.5},
        ]
    '''


    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Session(models.Model):

    vk_id = models.IntegerField(verbose_name="VK ID", db_index=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)




