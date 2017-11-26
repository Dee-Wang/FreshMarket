from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


# 用户信息
# 这里一个点就是没有真正的替换了系统的用户，在这里这样写之后还需要去settings文件中修改
class UserProfile(AbstractUser):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="生日")
    gender = models.CharField(max_length=32, choices=(("male", u"男"), ("female",u"女")), default="male", verbose_name="性别")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="电话号码")
    email = models.EmailField(max_length=128, null=True, blank=True, verbose_name="邮箱")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class VerifyCode(models.Model):
    code = models.CharField(max_length=10, verbose_name="短信验证码")
    mobile = models.CharField(max_length=11, verbose_name="手机号")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.code
