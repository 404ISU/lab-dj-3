from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    # Дополнительные поля для пользователя, например:
    # nickname = models.CharField(max_length=50, unique=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',  # Добавлен related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',  # Добавлен related_name
    )
    class Meta:
        swappable = 'AUTH_USER_MODEL'