from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from member.forms import UserForm, MemberForm
# Create your views here.

def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		member_form = MemberForm(data = request.POST)
		if user_form.is_valid() and member_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			member = member_form




def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username= username, password = password)
	if user is not None:
		if user.is_active:
			login(request,user)
	else:





