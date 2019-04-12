from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import PokerUser

class PokerUserCreationForm(UserCreationForm):

		class Meta(UserCreationForm):
			model = PokerUser
			fields = ('username','email','level')

class PokerUserChangeForm(UserChangeForm):

	class Meta:
		model = PokerUser
		fields = UserChangeForm.Meta.fields