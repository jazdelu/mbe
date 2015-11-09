from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives, EmailMessage
from collection.models import Collection
from page.models import Page
def home(request):
	c = Collection.objects.get(is_published = True)
	return render_to_response('index.html', { 'c':c }, context_instance=RequestContext(request))
	

def contact(request):
	status = 0
	try:
		page = Page.objects.get(ptype = 'contact')
	except:
		raise Http404
	if request.POST:
		fname = request.POST.get('firstname')
		lname = request.POST.get('lastname')
		phone = request.POST.get('phone')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		content = request.POST.get('content')
		from_email = 'robot@minibobi.com'
		text_content=''
		text_content += 'Name: '+fname+' '+lname+'<br/>'
		text_content += 'Phone: '+phone+'<br/>'
		text_content += 'Email: '+email+'<br/>'
		text_content += 'Subject: '+subject+'<br/>'
		text_content += 'Content: '+content+'<br/>'
		msg = EmailMessage(subject, text_content, from_email, ['lushizhao@qq.com',])
		msg.content_subtype = 'html'
		msg.send()

		return render_to_response("contact.html",{ "status":status,"page":page }, context_instance = RequestContext(request))
	else:
		return render_to_response("contact.html",{ "status":status,"page":page }, context_instance = RequestContext(request))

def commitments(request):
	page = ''
	try:
		page = Page.objects.get(ptype = 'commitments')
	except:
		raise Http404

	return render_to_response("commitments.html",{ "page":page },context_instance = RequestContext(request))


def conditions(request):
	page = ''
	try:
		page = Page.objects.get(ptype = 'conditions')
	except:
		raise Http404

	return render_to_response("conditions.html",{ "page":page },context_instance = RequestContext(request))
