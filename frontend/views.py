from django.shortcuts import render


def index(request):
	username = 'Empty'
	if request.user.is_authenticated:
		username = request.user.username
	return render(request, 'frontend/index.html')
# Create your views here.
