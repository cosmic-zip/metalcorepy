from shared.models.abstract_user_base import AbstractUserBase
from cloudinary.models import CloudinaryField
from django.db import models


class CustomUser(AbstractUserBase):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=300, blank=False)
    profile_image = CloudinaryField("image", blank=True, null=True)
