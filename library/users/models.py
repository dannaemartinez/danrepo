# from django.db import models
# from django.contrib.auth.models import User

# class Usesr(User):
#     #password = models.CharField(max_length = 256)

#     def Meta():
#         proxy = True

#     def __str__(self):
#         return f'Im user: {self.username}'

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
	email = models.CharField(max_length=255, unique=True)
	username = models.CharField(max_length=255, unique=True)

	class Type(models.IntegerChoices):
		BUYER = 1
		ADMIN = 2

	type = models.IntegerField(choices = Type.choices, default = 1)
