# -*- coding: utf-8 -*-
import os
import urllib
import uuid
from django.utils.deconstruct import deconstructible
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
import hashlib
from django.core.files.uploadedfile import SimpleUploadedFile


def get_avatar(instems, file):
    return "userimg/%s" % (file)


def get_file(instems, file):
    return "messagefile/%s" % (file)


@deconstructible
class RandomFileName:
    def __init__(self, sub_path=''):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        return os.path.join('images', self.sub_path, str(uuid.uuid4()) + '.' + filename.split('.')[-1])


@deconstructible
class RandomFileNameFile:
    def __init__(self, sub_path=''):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        return os.path.join('file', self.sub_path, str(uuid.uuid4()) + '.' + filename.split('.')[-1])


@deconstructible
class RandomFileNameFileEmployee:
    def __init__(self, sub_path=''):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        return os.path.join('fileemployee', self.sub_path, str(uuid.uuid4()) + '.' + filename.split('.')[-1])


@deconstructible
class RandomFileNameKorxona:
    def __init__(self, sub_path=''):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        return os.path.join('korxonaicon', self.sub_path, str(uuid.uuid4()) + '.' + filename.split('.')[-1])


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=False)
    last_name = models.CharField(max_length=50, blank=True, null=True, unique=False)
    patronymic_name = models.CharField(max_length=50, blank=True, null=True, unique=False)
    firebase_token = models.CharField(max_length=300, blank=True, null=True, unique=False,
                                      default='crIcQxyF1U_kToJXqRnK6L:APA91bFTzEd4xWGVm3KYANb0zFxecHHiKS41nfSPRVYqdVIX5xUi_hhcYRWj8JeBmCPBZUBxgabUPrGnmoNLR2IiXjmgxh51iOK4eGSnTvOo5KnDTJomLX2QKBze3XkCZrx4wNTZU25c')
    firebase_token_front = models.CharField(max_length=300, blank=True, null=True, unique=False,
                                            default='crIcQxyF1U_kToJXqRnK6L:APA91bFTzEd4xWGVm3KYANb0zFxecHHiKS41nfSPRVYqdVIX5xUi_hhcYRWj8JeBmCPBZUBxgabUPrGnmoNLR2IiXjmgxh51iOK4eGSnTvOo5KnDTJomLX2QKBze3XkCZrx4wNTZU25c')
    email = models.EmailField(('email address'), unique=True, null=False)
    phone_no = models.CharField(max_length=20)
    newpassword = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to=RandomFileName('User'), default='users/default.png')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'last_name']
    complete = models.IntegerField(default=1)
    unvoni = models.CharField(max_length=128, blank=True, null=True)
    xonasi = models.CharField(max_length=128, blank=True, null=True)
    superuser = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.email


def get_upload_to(instems, file):
    return "messagefile/%s" % (file)


import json


class Message(models.Model):
    GENDER_CHOICES = (
        ('yuborildi', 'YUBORILDI'),
        ('qabulqildi', 'QABULQILDI'),
        ('bajarildi', 'BAJARILDI'),
        ('kechikibbajarildi', 'KECHIKIBBAJARILDI'),
        ('bajarilmadi', 'BAJARILMADI')
    )
    gg_CHOICES = (
        ('kurilmagan', 'KURILMAGAN'),
        ('kurildi', 'KURILDI'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message")
    text = models.TextField(null=True, blank=True)
    text_employee = models.TextField(null=True, blank=True)
    status = models.CharField(choices=GENDER_CHOICES, max_length=50, null=True, blank=True)
    status2 = models.CharField(choices=gg_CHOICES, default='kurilmagan', max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    read_time = models.DateTimeField(auto_now=False, null=True)
    end_time = models.DateField(auto_now=False, null=True)
    confirm_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_user = models.IntegerField(default=0)
    done = models.IntegerField(default=0)
    failed = models.IntegerField(default=0)

    @property
    def state(self):
        mes = Message.objects.all()
        for x in mes:
            if date.today() > x.end_time and x.status != 'bajarildi' and x.status != 'kechikibbajarildi':
                x.status = 'bajarilmadi'
                x.save()
        return self.status

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.user.username


class MalumotUchun(models.Model):
    gg_CHOICES = (
        ('kurilmagan', 'KURILMAGAN'),
        ('kurildi', 'KURILDI'),
    )
    status = models.CharField(choices=gg_CHOICES, default='kurilmagan', max_length=50, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message12")
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    read_time = models.DateTimeField(auto_now=False, null=True)
    confirm_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_user = models.IntegerField(default=0)
    done = models.IntegerField(default=0)
    failed = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class AllNotification(models.Model):
    title = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    confirm_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_user = models.IntegerField(default=0)
    done = models.IntegerField(default=0)
    failed = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Notification(models.Model):
    title = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    confirm_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_user = models.IntegerField(default=0)
    done = models.IntegerField(default=0)
    failed = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class File(models.Model):
    file = models.FileField(upload_to=RandomFileNameFile('File'), null=True, blank=True)
    message = models.ForeignKey(Message, related_name='message', on_delete=models.CASCADE, null=True, blank=True)
    malumotuchun = models.ForeignKey(MalumotUchun, related_name='malumotucun', on_delete=models.CASCADE, null=True,
                                     blank=True)

    def __str__(self):
        if self.message:
            return f"{self.message.user.email}'s profile"
        else:
            return f"{self.malumotuchun.user.email}"


class File_employee(models.Model):
    file = models.FileField(upload_to=RandomFileNameFileEmployee('File_employee'), null=True, blank=True, default=None)
    message = models.ForeignKey(Message, related_name='message_employee', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.message.user.email


class Korxona(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, unique=False)
    icon = models.FileField(upload_to=RandomFileNameKorxona('Korxona'), null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class FoydaliLinklar(models.Model):
    korxona = models.ForeignKey(Korxona, on_delete=models.CASCADE, related_name="foydalilink")
    name = models.CharField(max_length=50, blank=True, null=True, unique=False)
    link = models.CharField(max_length=50, blank=True, null=True, unique=False)

    def __str__(self):
        return self.name


class IjtimoiyTarmoq(models.Model):
    korxona = models.ForeignKey(Korxona, on_delete=models.CASCADE, related_name="ijtimoiytarmoq")
    name = models.CharField(max_length=50, blank=True, null=True, unique=False)
    link = models.CharField(max_length=50, blank=True, null=True, unique=False)

    def __str__(self):
        return self.name


class Adress(models.Model):
    korxona = models.ForeignKey(Korxona, on_delete=models.CASCADE, related_name="adress")
    lot = models.CharField(max_length=60, blank=True, null=True, unique=False)
    lan = models.CharField(max_length=60, blank=True, null=True, unique=False)

    def __str__(self):
        return self.korxona.name
