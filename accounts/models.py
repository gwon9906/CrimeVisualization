from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    # 기타 필드 정의...
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # related_name 설정
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # related_name 설정
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )
