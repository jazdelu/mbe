from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from member.forms import UserForm, MemberForm, AuthenticationForm
from member.models import Member
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def user_register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		member_form = MemberForm(data = request.POST)
		if user_form.is_valid() and member_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()
			member = member_form.save(commit = False)
			member.user = user
			member.save()
			u = authenticate(username = request.POST['username'], password = request.POST['password'])
			login(request,u)
			registered = True
			return HttpResponseRedirect('/')

		else:
			pass

	else :
		user_form = UserForm()
		member_form = MemberForm()

	return render_to_response('register.html',{'user_form':user_form, 'member_form':member_form, 'registered':registered },context_instance=RequestContext(request))



@login_required
def user_profile(request):
	success = False
	user = User.objects.get(pk = request.user.id)
	if request.method == 'POST':
		member = Member.objects.get(user = user)
		user.set_password(request.POST['password'])
		user.email = request.POST['email']
		user.save()
		member.kidsname = request.POST['kidsname']
		member.email1 = request.POST['email1']
		member.address = request.POST['address']
		member.user = user
		member.save()
		return HttpResponseRedirect('/account/profile/')
	else:
		member = Member.objects.get(user = user)
		return render_to_response('user_profile.html',{'user':user,'member':member}, context_instance=RequestContext(request))





def user_login(request):
	error = ''
	if not request.user.is_authenticated():
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(username = username, password = password)
			if user:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/')
				else:
					return HttpResponse("You account is disabled")
			else:
				error = 'Invalid login details supplied'
				return render_to_response('login.html', {'error':error},context_instance=RequestContext(request))
		else:
			return render_to_response('login.html',context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/account/profile/')

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/account/login/')
