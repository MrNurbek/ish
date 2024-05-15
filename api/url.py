from django.urls import path
from django.conf.urls import include, url
from page.views import *
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from page.views import *

# -*- coding: utf-8 -*-
schema_view = get_schema_view(
    openapi.Info(
        title="Test API",
        default_version='v0.1',
        description="Test APIs for dashboard",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'get_message', MessageViewSet),
router.register(r'get_malumotuchun', MalumotuchunViewSet),
router.register(r'get_user_message', GetUserMessageViewSet),
router.register(r'message', MessageDetailView),
router.register(r'admin_message', MessageDetailView2),
router.register(r'malumot_id', MalumotDetailView2),
router.register(r'malumotuchun', MalumotDetailView),
router.register(r'messagepost', MessageDetailPostViewID),
router.register(r'notification', GetAllMessageViewSet),
router.register(r'get_users', GetUsersViewSet),
router.register(r'users_statistics', GetUsersStatisticsViewSet),
router.register(r'solo_statistics', UsersStatisticsViewSet2),
router.register(r'solo_statistics2', UsersStatisticsViewSet),
router.register(r'korxona', GetKorxonaViewSet),

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('register_user/', register_user),
    path('login', login),
    path('userlogin', userlogin),
    path('logout', LogoutView.as_view()),
    path('set-password', set_password),
    path('profile', me),
    path('put_profil', profil),
    path('updateFirebase_token', updateFirebase_token),
    path('post_message', post_message),
    path('post_malumotuchun', post_malumotuchun),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-profile'),
    path('exel/', export_movies_to_xlsx),
    path('solo_exel/', solo_export_movies_to_xlsx),
    path('solo_exel2/', solo_export_movies_to_xlsx2),
    path('all_statistics', StatisticsAll.as_view(), ),
    path('statistic_mengakelgan', StatisticsSolo.as_view(), ),
    path('statistic_menyuborgan', StatisticsSolo2.as_view(), )
]
urlpatterns += router.urls
