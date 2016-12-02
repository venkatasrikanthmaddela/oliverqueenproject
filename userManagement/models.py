import datetime
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from djangotoolbox.fields import SetField, DictField

from pmproject.models import CustomModel, CustomManager


class CustomUserManager(BaseUserManager,CustomManager):
    def create_user(self, email, phone_number, password, name, user_type="", is_staff=False, sources={},
                    additionalInfo={}, is_email_subscribed=False):
        user = self.model(
            email=CustomUserManager.normalize_email(email),
            phoneNumber=phone_number,
            name=name,
            type=user_type,
            is_staff=is_staff,
            sources=sources,
            additionalInfo=additionalInfo,
            is_email_subscribed=is_email_subscribed
        )
        user.set_password(password)
        user.save()
        return user

class PmUser(AbstractBaseUser):
    name = models.CharField(max_length=30, blank=False)
    email = models.CharField(unique=True, db_index=True, max_length=255)
    phoneNumber = models.CharField(max_length=20, blank=True)
    isActive = models.BooleanField(default=True)
    type = models.CharField(max_length=10, blank=True)
    is_staff = models.BooleanField(default=False)
    sources = SetField()
    additionalInfo = DictField()
    is_email_subscribed = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(default=datetime.datetime.now())
    autoLogOutTime = models.IntegerField(default=0)
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def get_full_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phoneNumber

    def get_short_name(self):
        return self.email

    @property
    def is_superuser(self):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    class MongoMeta:
        db_table = 'Users'
        index_together = ["name"]