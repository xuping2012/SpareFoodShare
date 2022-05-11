from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    id = models.BigAutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)
    nickname = models.CharField(verbose_name="昵称", max_length=256, default="", blank=True)
    tel_number = models.CharField(verbose_name="手机号", max_length=256, default="", blank=True)
    gender = models.CharField(verbose_name="性别", max_length=255, default="", blank=True)
    type = models.CharField(verbose_name="类别", max_length=255, default="", blank=True)
    balance = models.DecimalField(verbose_name="金额", max_digits=10, decimal_places=2, blank=True, default=0)

    status = models.IntegerField(verbose_name="状态", default=0, blank=True)
    version = models.IntegerField(verbose_name="版本号", default=0, blank=True)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, blank=True)
    modify_time = models.DateTimeField(verbose_name="修改时间", auto_now=True, blank=True)

    class Meta:
        db_table = "profile"
        verbose_name = "用户表"
        app_label = "userprofile"
