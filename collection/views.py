from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from collection.models import Product, Category, Subcategory, Collection
from django.template import RequestContext
from wish.models import Wish
# Create your views here.
def get_products_by_category(request,hierarchy):
	slugs = hierarchy.split('/')
	collection = Collection.objects.get(is_published = True)
	products = ''
	category = ''
	if len(slugs) == 1:
		category = Category.objects.get(slug=slugs[0])
		products = Product.objects.filter(collection = collection).filter(category = category)
	elif len(slugs) == 2:
		category = Category.objects.get(slug=slugs[0])
		subcategory = Subcategory.objects.filter(parent = category, slug = slugs[1])
		products = Product.objects.filter(collection = collection).filter(category = category).filter(subcategory = subcategory)
	else:
		return HttpResponseRedirect('/collection/')
	

	return render_to_response('product.html',{ 'collection':collection, 'products':products,'category':category },context_instance=RequestContext(request))
		

