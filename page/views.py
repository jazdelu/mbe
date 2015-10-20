from django.shortcuts import render_to_response
from django.http import Http404
from page.models import Page, Section
from django.template import RequestContext
from collection.models import Collection
# Create your views here.
def get_collection_page(request):
	collection = Collection.objects.get(is_published = True)
	page = Page.objects.filter(collection = collection).get(ptype = 'collection')
	left_sections = Section.objects.filter(page = page).filter(scol = 'left')
	right_sections = Section.objects.filter(page = page).filter(scol = 'right')


	return render_to_response('page.html',{ 'collection':collection, 'page':page,'left_sections':left_sections, 'right_sections':right_sections } ,context_instance=RequestContext(request) )


def get_about_page(request):
	page = Page.objects.get(ptype = 'about')
	left_sections = Section.objects.filter(page = page).filter(scol = 'left')
	right_sections = Section.objects.filter(page = page).filter(scol = 'right')
	return render_to_response('page.html',{'page':page,'left_sections':left_sections, 'right_sections':right_sections } ,context_instance=RequestContext(request) )