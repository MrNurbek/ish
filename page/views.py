from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import permissions
from firebasesdkadmin import send_firebase_message
from page.filters import MessageFilter, UserFilter, MessageFilter1
from .models import *
from rest_framework_jwt.settings import api_settings
from page.pagination import LargeResultsSetPagination
from page.serializers import UserSerializer, CustomuserSerializer, CustomuserSerializer2, ProfilSerializer, \
    ProfilSerializerAll, PostMessageSerializer, GetMessageSerializerAll, GetMessageSerializerAll2, ProfilSerializerMe, \
    CustomuserSerializer3, GetUsersSerializer, GetMessageSerializerAll3, FileSerializer, LogoutSerializer, \
    GetAllMessageSerializer, UserArraySerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework import generics, mixins
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics, filters

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view)
]


@api_view(['POST'])
@permission_classes([AllowAny, ])
def register_user(request):
    if request.method == 'POST':
        serializer = CustomuserSerializer3(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# @permission_classes([AllowAny, ])
# def set_password(request):
#     try:
#         old_password = request.data.get('old_password')
#         new_password = request.data.get('new_password')
#         user = request.user
#         if user.check_password(old_password):
#             user.set_password(new_password)
#             user.save()
#             result = {
#                 'status': 1,
#                 'msg': 'User password updated',
#                 'user': CustomuserSerializer(user, many=False, context={"request": request}).data
#             }
#             return Response(result, status=status.HTTP_200_OK)
#         else:
#             result = {
#                 'status': 1,
#                 'msg': 'User old password wrong'
#             }
#             return Response(result, status=status.HTTP_200_OK)
#     except KeyError:
#         res = {
#             'status': 0,
#             'msg': 'Please set all reqiured fields'
#         }
#         return Response(res)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def register(request):
    try:
        username = request.data.get('username')
        last_name = request.data.get('last_name')
        phone_no = request.data.get('phone_no')
        email = request.data.get('email')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        if not login:
            res = {
                'msg': 'Login empty',
                'status': 0,
            }
            return Response(res)

        user = User.objects.filter(email=email).first()
        if not user:
            user = User.objects.create(
                username=username,
                last_name=last_name,
                email=email,
                phone_no=phone_no,
                password=password,
                complete=1
            )
        elif user:
            res = {
                'msg': 'User exits',
                'status': 2,
            }
            return Response(res)
        elif password != confirm_password:
            res = {
                'msg': 'Password not equal',
                'status': 2,
            }
            return Response(res)

        if user:
            # payload = jwt_payload_handler(user)
            # token = jwt_encode_handler(payload)
            result = {
                'status': 1,
                'user': CustomuserSerializer(user, many=False, context={"request": request}).data,
                # 'token': token
            }
            return Response(result, status=status.HTTP_200_OK)
        else:
            res = {
                'status': 0,
                'msg': 'Can not authenticate with the given credentials or the account has been deactivated'
            }
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {
            'status': 0,
            'msg': 'Please set all reqiured fields'
        }
        return Response(res)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def login(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')
        firebase_token = request.data.get('firebase_token')
        if not login:
            res = {
                'msg': 'Login empty',
                'status': 0,
            }
            return Response(res)

        user = User.objects.filter(email=email).first()
        if not user:
            res = {
                'msg': 'email or password wrond',
                'status': 403,
            }
            return Response(res, status=status.HTTP_403_FORBIDDEN)

        if user and user.check_password(password):
            if user.complete == 0:
                res = {
                    'msg': 'email sms code not check',
                    'status': 0,
                }
                return Response(res)
            token = RefreshToken.for_user(user)
            result = {

                'user': UserSerializer(user, many=False, context={"request": request}).data,
                'access': str(token.access_token),
                'refresh': str(token),

            }
            user.firebase_token = firebase_token
            user.save()
            return Response(result, status=status.HTTP_200_OK)
        else:
            res = {
                'status': 0,
                'msg': 'Can not authenticate with the given credentials or the account has been deactivated'
            }
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {
            'status': 0,
            'msg': 'Please set all reqiured fields'
        }

        return Response(res)


class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def set_password(request):
    try:
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        user = request.user
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            result = {
                'status': 1,
                'msg': 'User password updated',
                'user': CustomuserSerializer(user, many=False, context={"request": request}).data
            }
            return Response(result, status=status.HTTP_200_OK)
        else:
            result = {
                'status': 1,
                'msg': 'User old password wrong'
            }
            return Response(result, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {
            'status': 0,
            'msg': 'Please set all reqiured fields'
        }
        return Response(res)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, ])
def profil(request):
    try:
        user = request.user

        username = request.data.get('username', user.username)
        last_name = request.data.get('last_name', user.last_name)
        email = request.data.get('email', user.email)
        phone_no = request.data.get('phone_no', user.phone_no)
        image = request.data.get('image', user.image)
        unvoni = request.data.get('unvoni', user.unvoni)
        xonasi = request.data.get('xonasi', user.xonasi)
        firebase_token = request.data.get('firebase_token', user.firebase_token)

        user.username = username
        user.last_name = last_name
        user.email = email
        user.phone_no = phone_no
        user.image = image
        user.xonasi = xonasi
        user.unvoni = unvoni
        user.firebase_token = firebase_token
        user.save()

        result = {
            'status': 1,
            'msg': 'User updated',
            'user': CustomuserSerializer3(user, many=False, context={"request": request}).data
        }
        return Response(result, status=status.HTTP_200_OK)
    except KeyError:
        res = {
            'status': 0,
            'msg': 'Please set all reqiured fields'
        }
        return Response(res)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, ])
def updateFirebase_token(request):
    try:
        user = request.user

        firebase_token = request.data.get('firebase_token', user.firebase_token)

        user.firebase_token = firebase_token
        user.save()

        result = {
            'status': 1,
            'msg': 'Token updated',
            'user': CustomuserSerializer3(user, many=False, context={"request": request}).data
        }
        return Response(result, status=status.HTTP_200_OK)
    except KeyError:
        res = {
            'status': 0,
            'msg': 'Please set all reqiured fields'
        }
        return Response(res)


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def me(request):
    try:
        user = request.user
        result = {
            'status': 1,
            'user': ProfilSerializerMe(user, many=False, context={"request": request}).data
        }
        return Response(result, status=status.HTTP_200_OK)
    except KeyError:
        res = {
            'status': 0,
            'msg': 'Please set all reqiured fields'
        }
        return Response(res)


# class ProfileAPI(APIView):
#     def get(self, request, *args, **kwargs):
#         user = get_object_or_404(User, pk=kwargs['user_id'])
#         profile_serializer = ProfilSerializer(user.profile)
#         return Response(profile_serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    serializer = ProfilSerializerMe(user, many=False)
    return Response(serializer.data)


@permission_classes([IsAuthenticated, ])
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = CustomuserSerializer3


# @permission_classes([IsAuthenticated, ])
# class MessageDetailView(generics.RetrieveAPIView):
#     queryset = Message.objects.all()
#     serializer_class = GetMessageSerializerAll2
#     filterset_class = MessageFilter1
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter]
#
#     def get(self, request, *args, **kwargs):
#
#         # queryset = Message.objects.filter(user_id=self.request.user.id, id=kwargs['pk'])
#         queryset = Message.objects.filter(user_id=self.request.user.id)
#
#         for x in queryset:
#             if x.status != 'bajarilmadi' and x.status != 'bajarildi':
#                 queryset.update(status="qabulqildi")
#         serializer = GetMessageSerializerAll2(queryset, many=True, context={"request": request})
#         return Response(serializer.data, status=status.HTTP_200_OK)


class MessageDetailView(generics.ListAPIView, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = GetMessageSerializerAll2
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.order_by('-id').all()
    # pagination_class = LimitOffsetPagination
    filterset_class = MessageFilter1
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    def get_queryset(self):
        # queryset = Message.objects.filter(user_id=self.request.user.id, id=kwargs['pk'])
        queryset = Message.objects.filter(user_id=self.request.user.id, id=self.request.GET['id'])

        for x in queryset:
            if x.status != 'bajarilmadi' and x.status != 'bajarildi':
                queryset.update(status="qabulqildi")
        return queryset


class MessageDetailPostViewID(generics.ListAPIView, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = GetMessageSerializerAll2
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.order_by('-id').all()
    pagination_class = LimitOffsetPagination
    filterset_class = MessageFilter1
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    def post(self, request, *args, **kwargs):
        queryset = Message.objects.filter(user_id=self.request.user.id, id=self.request.GET['id'])
        message = Message.objects.get(user_id=self.request.user.id, id=self.request.GET['id'])
        for x in queryset:
            text_employee = request.data['text_employee']
            if x.status != 'bajarilmadi' and x.status != 'kechikibbajarildi':
                queryset.update(status="bajarildi", text_employee=text_employee)
            elif x.status == 'bajarilmadi':
                queryset.update(status="kechikibbajarildi", text_employee=text_employee)

        files = request.FILES.getlist('file')
        for file in files:
            filesave = File_employee.objects.create(
                file=file,
                message=message
            ).save()
        serializer = GetMessageSerializerAll2(queryset, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAdminUser, ])
def post_message(request):
    try:
        item_serializer = UserArraySerializer(data=request.data)
        item_serializer.is_valid(raise_exception=True)
        user = item_serializer.data['user']
        # user = request.data["user"]
        text = request.data['text']
        end_time = request.data['end_time']
        for x in user:
            user1 = User.objects.filter(id=x)
            message = Message.objects.create(
                # user=request.user,
                user_id=x,
                text=text,
                end_time=end_time,
                status='yuborildi',
                created_user=request.user.id,

            )
            message.save()
            # funksiya
            send_firebase_message(user1.last().firebase_token, 'Hujjat Almashinuv Tizimi', 'Yangi xabar')
            files = request.FILES.getlist('file')
            for file in files:
                File.objects.create(
                    file=file,
                    message=message
                )
        result = {
            'status': 1,
            'msg': 'add_message',
            'message': PostMessageSerializer(message, many=False, context={"request": request}).data,
        }
        return Response(result, status=status.HTTP_200_OK)

    except KeyError:
        res = {
            'status': 0,
            'msg': 'erorr add_message'
        }
        return Response(res)


class MessageViewSet(generics.ListAPIView, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = GetMessageSerializerAll2
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.order_by('-id').all()
    # pagination_class = LimitOffsetPagination
    filterset_class = MessageFilter
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    def get_queryset(self):
        queryset = Message.objects.filter(created_user=self.request.user.id)
        event = Message.objects.first()

        if event.state:
            return queryset


class GetUserMessageViewSet(generics.ListAPIView, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = GetMessageSerializerAll2
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.order_by('-id').all()
    # pagination_class = LimitOffsetPagination
    filterset_class = MessageFilter
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    def get_queryset(self):
        queryset = Message.objects.filter(user_id=self.request.user.id)
        return queryset


#     if self.request.user.is_staff == False:
#         queryset = Message.objects.filter(user_id=self.request.user.id)
#         return queryset
#     else:
#         queryset = Message.objects.filter(created_user=self.request.user.id)
#         event = Message.objects.first()
#         if event.state:
#             return queryset


class GetAllMessageViewSet(generics.ListAPIView, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = GetAllMessageSerializer
    permission_classes = [IsAuthenticated]
    queryset = AllNotification.objects.order_by('-id').all()
    pagination_class = LimitOffsetPagination
    # filterset_class = MessageFilter
    # pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


from django.db.models import Q


class GetUsersViewSet(generics.ListAPIView, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = GetUsersSerializer
    permission_classes = [IsAdminUser]
    queryset = User.objects.order_by('-id').all()
    filterset_class = UserFilter
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    # filterset_fields = ['user']
    # search_fields = ['user']
    def get_queryset(self):
        queryset = User.objects.filter(~Q(id=self.request.user.id))
        return queryset
