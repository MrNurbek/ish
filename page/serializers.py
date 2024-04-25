# -*- coding: utf-8 -*-
from django.utils.text import gettext_lazy as _
from rest_framework import serializers
from page.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', "last_name", 'username', 'phone_no', 'image', 'is_staff', 'unvoni', 'xonasi', 'superuser']


class CustomuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CustomuserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CustomuserSerializer3(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', "last_name", 'username', 'phone_no', 'image', 'password', 'complete', 'xonasi', 'unvoni',
                  'is_staff', 'firebase_token']

    def create(self, validated_data):
        user = User(**validated_data)
        # Hash the user's password.
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomuserSerializer4(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', "last_name", 'username', 'phone_no', 'image', 'password', 'complete', 'xonasi', 'unvoni',
                  'is_staff']

    def create(self, validated_data):
        user = User(**validated_data)
        # Hash the user's password.
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', "last_name", 'username', 'image', 'phone_no', 'unvoni', 'xonasi']


class ProfilSerializerMe(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', "last_name", 'username', 'image', 'phone_no', 'unvoni', 'xonasi',
                  'is_staff', 'superuser']


class GetUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', "last_name", 'username', 'image', 'phone_no', 'unvoni', 'xonasi',
                  'is_staff', 'superuser']


class GetUsersStatisticsSerializer(serializers.ModelSerializer):
    yuborildi = serializers.SerializerMethodField()
    qabulqildi = serializers.SerializerMethodField()
    bajarildi = serializers.SerializerMethodField()
    kechikibbajarildi = serializers.SerializerMethodField()
    bajarilmadi = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', "last_name", 'username', 'image', 'phone_no', 'unvoni',
                  'yuborildi', 'qabulqildi', 'bajarildi', 'kechikibbajarildi', 'bajarilmadi', 'superuser']

    def get_yuborildi(self, obj):
        message = Message.objects.filter(user=obj, status='yuborildi').count()
        return message

    def get_qabulqildi(self, obj):
        message = Message.objects.filter(user=obj, status='qabulqildi').count()
        return message

    def get_bajarildi(self, obj):
        message = Message.objects.filter(user=obj, status='bajarildi').count()
        return message

    def get_kechikibbajarildi(self, obj):
        message = Message.objects.filter(user=obj, status='kechikibbajarildi').count()
        return message

    def get_bajarilmadi(self, obj):
        message = Message.objects.filter(user=obj, status='bajarilmadi').count()
        return message


class ProfilSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


class File_employeSerializer(serializers.ModelSerializer):
    class Meta:
        model = File_employee
        fields = "__all__"


class PostMessageSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = "__all__"

    def get_file(self, obj):
        file = File.objects.filter(message=obj).all()
        if file:
            return FileSerializer(file, many=True, context={'request': self.context['request']}).data
        return None

    # def get_file(self, obj):
    #     file = File.objects.filter(message=obj).all()
    #     return FileSerializer(file, data=self.context('request').data, many=True,
    #                           context={'request': self.context['request']}).data


class GetMessageSerializerAll(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = "__all__"

    def get_user(self, obj):
        return CustomuserSerializer2(obj.user, many=False, context={"request": self.context['request']}).data


class GetAllMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllNotification
        fields = "__all__"


class GetMessageSerializerAll3(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class GetMessageSerializerAll2(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    user_email = serializers.SerializerMethodField()
    user_xonasi = serializers.SerializerMethodField()
    user_unvoni = serializers.SerializerMethodField()
    file = serializers.SerializerMethodField()
    file_employee = serializers.SerializerMethodField()
    adminusername = serializers.SerializerMethodField()
    adminlast_name = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    adminunvoni = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ['id', 'text', 'text_employee', 'user', 'user_id', 'user_email', 'user_xonasi', 'user_unvoni',
                  'end_time', 'created_user', 'image', 'adminusername', 'adminlast_name', 'adminunvoni', 'file',
                  'file_employee']

    def get_image(self, obj):
        user = User.objects.filter(id=obj.created_user)
        return user.last().image.url

    def get_adminunvoni(self, obj):
        user = User.objects.filter(id=obj.created_user)
        return user.last().unvoni

    def get_adminusername(self, obj):
        user = User.objects.filter(id=obj.created_user)
        return user.last().username

    def get_adminlast_name(self, obj):
        user = User.objects.filter(id=obj.created_user)
        return user.last().last_name

    def get_file(self, obj):
        images = File.objects.filter(message=obj).all()
        return FileSerializer(images, many=True, context={'request': self.context['request']}).data

    def get_file_employee(self, obj):
        images = File_employee.objects.filter(message=obj).all()
        return File_employeSerializer(images, many=True, context={'request': self.context['request']}).data

    # def get_user2(self, obj):
    #     return CustomuserSerializer2(obj.user, many=False, context={"request": self.context['request']}).data

    def get_user(self, obj):
        if obj.user:
            return obj.user.username
        return 0

    def get_user_id(self, obj):
        if obj.user:
            return obj.user.id
        return 0

    def get_user_email(self, obj):
        if obj.user:
            return obj.user.email
        return 0

    def get_user_xonasi(self, obj):
        if obj.user:
            return obj.user.xonasi
        return 0

    def get_user_unvoni(self, obj):
        if obj.user:
            return obj.user.unvoni
        return 0


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': _('Token is invalid or expired')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')
        except Exception as e:
            print('\nException in logging out:', e)


class UserArraySerializer(serializers.Serializer):
    user = serializers.ListField(child=serializers.IntegerField())


class FoydalilinklarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoydaliLinklar
        fields = "__all__"


class IjtimoiyTarmoqSerializer(serializers.ModelSerializer):
    class Meta:
        model = IjtimoiyTarmoq
        fields = "__all__"


class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = "__all__"


class KorxonaSerializer(serializers.ModelSerializer):
    foydaliLinklar = serializers.SerializerMethodField()
    ijtimoiytarmoq = serializers.SerializerMethodField()
    adress = serializers.SerializerMethodField()

    class Meta:
        model = Korxona
        fields = ['id', 'name', 'icon', 'foydaliLinklar', 'ijtimoiytarmoq', 'adress', ]

    def get_foydaliLinklar(self, obj):
        foydaliLinklar = FoydaliLinklar.objects.filter(korxona=obj).all()
        return FoydalilinklarSerializer(foydaliLinklar, many=True, context={'request': self.context['request']}).data

    def get_ijtimoiytarmoq(self, obj):
        ijtimoiytarmoq = IjtimoiyTarmoq.objects.filter(korxona=obj).all()
        return IjtimoiyTarmoqSerializer(ijtimoiytarmoq, many=True, context={'request': self.context['request']}).data

    def get_adress(self, obj):
        adress = IjtimoiyTarmoq.objects.filter(korxona=obj).all()
        return AdressSerializer(adress, many=True, context={'request': self.context['request']}).data
