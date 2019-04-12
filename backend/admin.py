from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import PokerUserCreationForm, PokerUserChangeForm
from .models import PokerUser

class PokerUserAdmin(UserAdmin):
	model = PokerUser
	add_form = PokerUserCreationForm
	form = PokerUserChangeForm

admin.site.register(PokerUser, PokerUserAdmin)
# Register your models here.
