from django.db import models

class Client(models.Model):
	name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128, null=True)
	email = models.CharField(max_length=200, null=True)
	
	def __str__(self) -> str:
		return self.name + " " + self.last_name

# Create your models here.