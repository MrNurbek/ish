from django.urls import path
from django.conf.urls import include, url
from page.views import *
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

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
router.register(r'get_user_message', GetUserMessageViewSet),
router.register(r'message', MessageDetailView),
router.register(r'messagepost', MessageDetailPostViewID),
router.register(r'notification', GetAllMessageViewSet),
router.register(r'get_users', GetUsersViewSet),

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('register_user/', register_user),
    path('register', register),
    path('login', login),
    path('logout', LogoutView.as_view()),
    path('set-password', set_password),
    path('profile', me),
    path('put_profil', profil),
    path('updateFirebase_token', updateFirebase_token),
    path('post_message', post_message),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-profile'),
    # path('profile/', views.getProfile,),
    # path('message/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
    # path('message', MessageDetailView.as_view(), name='message-detail'),
    # path('messagepost/<int:pk>/', MessageDetailPostViewID.as_view(), name='message-detailid'),

]
urlpatterns += router.urls
