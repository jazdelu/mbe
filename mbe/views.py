from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from collection.models import Collection
def home(request):
	c = Collection.objects.get(is_published = True)
	return render_to_response('index.html', { 'c':c }, context_instance=RequestContext(request))
	