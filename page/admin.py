# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *


class FileInline(admin.TabularInline):
    model = File


class FoydaliLinklarInline(admin.TabularInline):
    model = FoydaliLinklar


class IjtimoiyTarmoqInline(admin.TabularInline):
    model = IjtimoiyTarmoq


class AdressTarmoqInline(admin.TabularInline):
    model = Adress


class FileEmployeeInline(admin.TabularInline):
    model = File_employee


class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'message')


class FileEmployeeAdmin(admin.ModelAdmin):
    list_display = ('file', 'message')


# list_display = (' image ')
# sortable_by = ('image')
# search_fields = ['file']


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'is_staff', 'last_name', 'password', 'unvoni', 'xonasi', 'image')


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'status', 'status2', 'created_user', 'text', 'text_employee', 'created_at', 'read_time',
        'updated_at',
        'confirm_at')
    inlines = [FileInline, FileEmployeeInline]


class MalumotUchunAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'created_user', 'text', 'created_at', 'read_time', 'updated_at',
        'confirm_at')
    inlines = [FileInline]


class AllNotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class KorxonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')
    inlines = [FoydaliLinklarInline, IjtimoiyTarmoqInline, AdressTarmoqInline]


admin.site.register(User, UserAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(MalumotUchun, MalumotUchunAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(File_employee, FileEmployeeAdmin)
admin.site.register(AllNotification, AllNotificationAdmin)
admin.site.register(Korxona, KorxonaAdmin)
admin.site.register(FoydaliLinklar)
admin.site.register(IjtimoiyTarmoq)
admin.site.register(Adress)
