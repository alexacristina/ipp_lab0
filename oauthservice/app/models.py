from django.db import models
from django.contrib.auth.models import User, UserManager
from binascii import hexlify
from django.contrib.auth.tokens import default_token_generator	
from rest_framework.authtoken.models import Token

class Client(models.Model):
	client_id=models.IntegerField(unique=True)

	def save(self, *args, **kwargs):
		super(Client, self).save(*args, **kwargs)


class AccessToken(models.Model):
	user = models.ForeignKey(User)
	client = models.ForeignKey(Client)
	token = models.CharField(default='', max_length=255)

	def generate_token(self):
		self.token=default_token_generator.make_token(self.user)

	


