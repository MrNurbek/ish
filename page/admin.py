from django.contrib import admin
from .models import *


# -*- coding: utf-8 -*-

class FileInline(admin.TabularInline):
    model = File


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
    list_display = ('id', 'email', 'username', 'is_staff', 'last_name', 'password', 'unvoni', 'xonasi')


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'status', 'text', 'text_employee', 'created_at', 'read_time', 'updated_at', 'confirm_at')
    inlines = [FileInline, FileEmployeeInline]


class AllNotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(User, UserAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(File_employee, FileEmployeeAdmin)
admin.site.register(AllNotification, AllNotificationAdmin)
