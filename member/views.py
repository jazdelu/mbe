from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from member.forms import UserForm, MemberForm, AuthenticationForm
from member.models import Member
from page.models import Page
from django.http import HttpResponseRedirect, HttpResponse, Http404
# Create your views here.

def user_register(request):
	registered = False
	page = ''
	try:
		page = Page.objects.get(ptype = 'register')
	except:
		raise Http404
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
			return render_to_response('register.html',{'user_form':user_form, 'member_form':member_form, 'registered':registered, 'page':page },context_instance=RequestContext(request))

	else :
		user_form = UserForm()
		member_form = MemberForm()

	return render_to_response('register.html',{'user_form':user_form, 'member_form':member_form, 'registered':registered,'page':page },context_instance=RequestContext(request))



@login_required
def user_profile(request):
	success = False
	user = User.objects.get(pk = request.user.id)
	page = ''
	try:
		page = Page.objects.get(ptype = 'register')
	except:
		raise Http404
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
	else:
		print user.id
		member = Member.objects.get(user = user)
	return render_to_response('user_profile.html',{'user':user,'member':member,'page':page}, context_instance=RequestContext(request))





def user_login(request):
	error = ''
	page = ''
	try:
		page = Page.objects.get(ptype = 'register')
	except:
		raise Http404
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
				return render_to_response('login.html', {'error':error, 'page':page},context_instance=RequestContext(request))
		else:
			return render_to_response('login.html',{'page':page},context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/account/profile/')

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/account/login/')
