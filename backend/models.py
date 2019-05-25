from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class PokerUserManager(UserManager):
	pass

class PokerUser(AbstractUser):
	BEGGINER = 'BG'
	ADVANCED = 'AD'
	INTERMEDIATE = 'IM'
	LEVEL_CHOICES = (
		(BEGGINER, 'Begginer'),
		(ADVANCED, 'Advanced'),
		(INTERMEDIATE, 'Intermediate'),
	)
	balance = models.CharField(max_length = 100)
	level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=BEGGINER,)
	objects = PokerUserManager()