# domains/user/views.py

from domains.user.schemas import TokenSchema, LoginSchema
from ninja import Router, Schema
from django.contrib.auth import authenticate
from datetime import datetime, timedelta
import jwt
from django.conf import settings
from ninja.errors import HttpError
from shared.auth.jwt import JWTAuth

auth_router = Router(tags=["auth"])
user_router = Router(auth=JWTAuth(), tags=["user"])


@auth_router.post("/login", response=TokenSchema)
def login(request, data: LoginSchema):
    user = authenticate(request, username=data.email, password=data.password)
    if not user:
        raise HttpError(401, "Invalid credentials")
    
    payload = {
        "user_id": user.id,
        "exp": datetime.utcnow() + timedelta(hours=1),
        "iat": datetime.utcnow(),
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}

@user_router.get("/me")
def get_me(request):
    user = request.auth
    return {
        "id": user.id,
        "email": user.email,
        "name": user.name,
    }
