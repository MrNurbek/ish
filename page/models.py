from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


def get_avatar(instems, file):
    return "userimg/%s" % (file)


def get_file(instems, file):
    return "messagefile/%s" % (file)


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=False)
    last_name = models.CharField(max_length=50, blank=True, null=True, unique=False)
    firebase_token = models.CharField(max_length=300, blank=True, null=True, unique=False,
                                      default='crIcQxyF1U_kToJXqRnK6L:APA91bFTzEd4xWGVm3KYANb0zFxecHHiKS41nfSPRVYqdVIX5xUi_hhcYRWj8JeBmCPBZUBxgabUPrGnmoNLR2IiXjmgxh51iOK4eGSnTvOo5KnDTJomLX2QKBze3XkCZrx4wNTZU25c')
    email = models.EmailField(('email address'), unique=True, null=False)
    phone_no = models.CharField(max_length=20)
    newpassword = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='userimg', default='users/default.png')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'last_name']
    complete = models.IntegerField(default=1)
    unvoni = models.CharField(max_length=128, blank=True, null=True)
    xonasi = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return u"%s..." % self.image

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message")
    text = models.TextField(null=True, blank=True)
    text_employee = models.TextField(null=True, blank=True)
    status = models.CharField(choices=GENDER_CHOICES, max_length=50, null=True, blank=True)
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
    file = models.FileField(upload_to="messagefile", null=True, blank=True)
    message = models.ForeignKey(Message, related_name='message', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.message.user.email


class File_employee(models.Model):
    file = models.FileField(upload_to="employeemessagefile", null=True, blank=True, default=None)
    message = models.ForeignKey(Message, related_name='message_employee', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.message.user.email



