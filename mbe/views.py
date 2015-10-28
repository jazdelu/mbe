from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives
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
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		content = request.POST.get('content')
		from_email = 'robot@minibobi.com'
		text_content=''
		text_content += email+':  '
		text_content += content
		msg = EmailMultiAlternatives(subject, text_content, from_email, ['lushizhao@qq.com',])
		try:
			msg.send()
			status = 1
		except:
			raise Http404

		return render_to_response("contact.html",{ "status":status,"page":page }, context_instance = RequestContext(request))
	else:
		return render_to_response("contact.html",{ "status":status,"page":page }, context_instance = RequestContext(request))