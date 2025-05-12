# shared/authentication/jwt.py

import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from ninja.errors import HttpError
from ninja.security import HttpBearer

User = get_user_model()

class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = payload.get("user_id")
            if not user_id:
                raise HttpError(401, "Invalid token payload")
            return User.objects.get(id=user_id)
        except jwt.ExpiredSignatureError:
            raise HttpError(401, "Token expired")
        except jwt.InvalidTokenError:
            raise HttpError(401, "Invalid token")
        except User.DoesNotExist:
            raise HttpError(401, "User not found")
