from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
"""
class CustomManger(BaseUserManager):
	
	use_in_migrations = True

	def get_by_natural_key(self, email):
		return self.get(**{self.model.USERNAME_FIELD: email})

	def _create_user(self, email, password, **extra_fields):
		now = timezone.now()
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, date_joined=now, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, username, email, password, **extra_fields):
		username = None
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have staff=true')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=true')
		return self._create_user(username, email, password, **extra_fields)
"""
class CustomUser(AbstractUser):
	def __str__(self):
		return self.email