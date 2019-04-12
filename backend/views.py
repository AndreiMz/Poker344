from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.urls import reverse_lazy

from .forms import PokerUserCreationForm
# Create your views here.
class Home(TemplateView):
	template_name = 'home.haml'

class Register(generic.CreateView):
	form_class = PokerUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.haml'

class Login(generic.CreateView):
	template_name = 'registration/login.haml'
	