import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
from urllib.parse import parse_qs
from django.db import close_old_connections
from channels.db import database_sync_to_async
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
import jwt
from django.utils.translation import ugettext as _
from rest_framework import exceptions

jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER

from rest_framework import status
@database_sync_to_async
def close_connections():
    close_old_connections()


class JsonTokenAuthMiddleware(BaseJSONWebTokenAuthentication):
    """
    Token authorization middleware for Django Channels 2
    """

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        try:
            close_connections()
            query_string = parse_qs(scope["query_string"])
            token = query_string[b"token"][0]
            payload = jwt_decode_handler(token)
            print(payload)
            scope['user'] = payload
            # scope['user'] = await get_user(int(self.scope["query_string"]))
        except:
            scope['user'] = None
        return await self.inner(scope, receive, send)


JsonTokenAuthMiddlewareStack = lambda inner: JsonTokenAuthMiddleware(inner)
