from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

SEX_CHOICE = [
	('Male','M'),
	('Female','F')
]

class Collection(models.Model):
	name = models.CharField(max_length = 128,verbose_name=_('Name'))
	slug = models.SlugField(max_length = 128,verbose_name=_('Slug'),help_text = _('Displayed in the URL'))
	pub_date = models.DateTimeField(auto_now_add = True,verbose_name=_('Publish Date'))
	last_modified = models.DateTimeField(auto_now = True,verbose_name=_('Last Modified Date'))
	is_published = models.BooleanField(verbose_name = "Publish this collection?")

	class Meta:
		verbose_name = _('Collection')
		verbose_name_plural = _('Collection')

	def __unicode__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length = 128, verbose_name = 'Name')
	slug = models.SlugField(max_length = 128, verbose_name = 'Slug')

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Category'

	def __unicode__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=128, verbose_name = _('Name'))
	serial = models.CharField(max_length = 128,verbose_name = _('Serial'),blank = True,null = True)
	sex = models.CharField(max_length = 128,choices = SEX_CHOICE, blank = True, null = True)
	category = models.ForeignKey(Category,related_name = 'products', blank = True, null = True)
	short_description = models.CharField(max_length = 128,verbose_name = _('Short Description'))
	collection = models.ForeignKey(Collection,related_name= 'products',default = 1)
	price = models.FloatField(verbose_name = _('Price'))
	image1 = models.ImageField(upload_to = 'product/',verbose_name = 'Image1')
	image2 = models.ImageField(upload_to = 'product/',verbose_name = 'Image2')
	pub_date = models.DateTimeField(verbose_name = "Publish Date")
	last_modified = models.DateTimeField(auto_now = True)

	class Meta:
		verbose_name = _('Product')
		verbose_name_plural = _('Product')
		ordering =['-pub_date']
		
	def __unicode__(self):
		return self.name