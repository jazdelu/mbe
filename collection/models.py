from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Collection(models.Model):
	name = models.CharField(max_length = 128,verbose_name=_('Name'))
	background = models.ImageField(upload_to = 'background/', verbose_name = 'Cover',blank = True, null = True)
	pub_date = models.DateTimeField(auto_now_add = True,verbose_name=_('Publish Date'))
	last_modified = models.DateTimeField(auto_now = True,verbose_name=_('Last Modified Date'))
	is_published = models.BooleanField(verbose_name = "Publish this collection?")

	class Meta:
		verbose_name = _('Collection')
		verbose_name_plural = _('Collection')

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		if self.is_published:
			try:
				collection = Collection.objects.get(is_published = True)
				collection.is_published = False
				collection.save()
			except:
				pass
		super(Collection,self).save(*args, **kwargs)



class Category(models.Model):
	name = models.CharField(max_length = 128, verbose_name = 'Name')
	slug = models.SlugField(max_length = 128, verbose_name = 'Slug')
	page_title = models.CharField(max_length = 128,verbose_name = 'Page Title', blank = True, null = True)
	description = models.TextField(verbose_name = 'Description', blank = True, null = True)
	cover = models.ImageField(upload_to = 'category/', verbose_name = 'Cover',blank = True, null = True)
	image = models.ImageField(upload_to = 'category/',verbose_name = 'Image', blank = True, null = True)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Category'

	def __unicode__(self):
		return self.name

class Subcategory(models.Model):
	parent = models.ForeignKey(Category,verbose_name = 'Parent', related_name = 'subs')
	name = models.CharField(max_length = 128, verbose_name = 'Name')
	slug = models.SlugField(max_length = 128, verbose_name = 'Slug')
	order = models.IntegerField(verbose_name = 'Order',help_text = 'Ordering the sub-navigation')

	class Meta:
		verbose_name = "Sub-Category"
		verbose_name_plural = "Sub-Category"
		ordering = ['parent','order']

	def __unicode__(self):
		return self.parent.name +'--'+self.name

class Product(models.Model):
	name = models.CharField(max_length=128, verbose_name = _('Name'))
	serial = models.CharField(max_length = 128,verbose_name = _('Serial'),blank = True,null = True)
	category = models.ForeignKey(Category,related_name = 'products')
	subcategory =models.ForeignKey(Subcategory,related_name = 'products')
	short_description = models.CharField(max_length = 128,verbose_name = _('Short Description'))
	collection = models.ForeignKey(Collection,related_name= 'products',default = 1)
	price = models.FloatField(verbose_name = _('Price'))
	image1 = models.ImageField(upload_to = 'product/',verbose_name = 'Image1')
	image2 = models.ImageField(upload_to = 'product/',verbose_name = 'Image2')
	pub_date =  models.DateTimeField(verbose_name = "Publish Date",auto_now_add= True)
	last_modified = models.DateTimeField(auto_now = True)
	last_liked = models.DateTimeField(auto_now_add = True)

	class Meta:
		verbose_name = _('Product')
		verbose_name_plural = _('Product')
		ordering =['-pub_date','collection','category','subcategory']
		
	def __unicode__(self):
		return self.name


	def get_wished_users(self):
		users = []
		for w in self.wishes.all():
			users.append(w.user)
		return users


