from ninja import NinjaAPI
from domains.user.views import auth_router, user_router

api = NinjaAPI()
api.add_router("/auth/", auth_router)
api.add_router("/user/", user_router)