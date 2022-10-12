from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):       # 커스텀 유저모델의 내장 모델
    pass