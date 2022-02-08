from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware

@database_sync_to_async
def get_user(user_model, token_key):
	print(token_key['user_id'])
	try:
		return user_model.objects.get(id=token_key['user_id'])
	except user_model.DoesNotExist:
		return AnonymousUser()

class TokenAuthMiddleware(BaseMiddleware):
	"""
	Custom JWT authentication for Channels v3
	"""
	def __init__(self, inner):
		super().__init__(inner)
		self.user_model = get_user_model()
		self.jwt = JWTAuthentication()

	async def __call__(self, scope, receive, send):
		try:
			authorization_header = dict(scope['headers']).get(b'authorization', None)
			validated_token = self.jwt.get_validated_token(self.jwt.get_raw_token(authorization_header))
		except KeyError:
			validated_token = None
		scope['user'] = AnonymousUser() if validated_token is None else await get_user(self.user_model, validated_token)
		return await super().__call__(scope, receive, send)
