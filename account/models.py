from django.db import models
from django.contrib.auth.models import User

from account.choices import GENDER_CHOICES, MessageStatus


class Town(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Город')
    translit = models.CharField(max_length=50, unique=True, verbose_name='Транслит')


class User2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    town = models.ForeignKey('Town', verbose_name='Город', on_delete=models.SET_NULL, blank=True, null=True)
    surname = models.CharField(max_length=40, verbose_name='Фамилия', blank=True, null=True)
    first_name = models.CharField(max_length=40, verbose_name='Имя', blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол', blank=True, null=True)
    dt_created = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=20, verbose_name='Телефон', blank=True, null=True)


class Chat(models.Model):
    user = models.ManyToManyField(User2)


class PrivateMessage(models.Model):
    sender = models.ForeignKey(User2, verbose_name='Отправитель', on_delete=models.CASCADE, related_name='senders')
    recipient = models.ForeignKey(User2, verbose_name='Получатель', on_delete=models.CASCADE, related_name='recipients')
    text = models.CharField(max_length=300, verbose_name='Текст сообщения')
    dt_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    status = models.CharField(max_length=10, choices=MessageStatus.CHOICES, default=MessageStatus.SEND)
