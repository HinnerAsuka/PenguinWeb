from django.db import models

# Create your models here.

# django自带一个用户模型，这个用户模型有 密码加密和密码验证
from django.contrib.auth.models import AbstractUser
from utils.models import BaseModel


class User(AbstractUser):
    mobile = models.CharField(max_length=11, verbose_name='手机号', unique=True)
    # 添加邮箱验证状态字段
    email_active = models.BooleanField(default=False, verbose_name='邮箱验证状态')
    avatar = models.CharField(max_length=255, verbose_name='头像')

    class Meta:
        db_table = 'pg_users'
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name
