from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from wish.models import Wish
from collection.models import Product, Collection
from page.models import Page
from django.contrib.auth.models import User

# Create your views here.

def add(request):
	if request.user.is_authenticated():
		pid = request.GET['pid']
		product = Product.objects.get(id = int(pid))
		user = request.user
		try:
			wish = Wish.objects.get(user = user, product = product)
		except:
			wish = Wish()
			wish.product = product
			wish.user = user
			wish.save()
			product.last_liked = wish.datetime
			product.save()
			return HttpResponseRedirect(request.GET['next'])

		return HttpResponse("Repeate Operation")
	else:
		return HttpResponseRedirect('/account/login/')


def remove(request):
	if request.user.is_authenticated():
		pid = request.GET['pid']
		product = Product.objects.get(id = int(pid))
		user = request.user
		wish = Wish.objects.get(user = user, product = product)
		wish.delete()
		return HttpResponseRedirect(request.GET['next'])
	else:
		return HttpResponseRedirect('/account/login/')


def get_wishes_by_product(request):
	products = Product.objects.all().order_by('-last_liked')
	page = ''
	try:
		page = Page.objects.get(ptype = 'wishlist')
	except:
		raise Http404
	return render_to_response('wishlist.html', { 'products':products, 'page':page }, context_instance=RequestContext(request))