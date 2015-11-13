from django.db import models
from collection.models import Collection
# Create your models here.
PAGE_TYPE_CHOICES = [
	('about','about'),
	('collection','collection'),
	('commitments','commitments'),
	('conditions','conditions'),
	('contact','contact'),
	('wishlist','wishlist'),
]
SECTION_TYPE_CHOICES = [
	('image','image'),
	('text','text'),
]
SECTION_COL_CHOICES = [
	('left','left'),
	('right','right'),
]

class Page(models.Model):
	name = models.CharField(max_length = 128, verbose_name = 'Name')
	ptype = models.CharField(max_length = 128, verbose_name = 'Page Type',choices = PAGE_TYPE_CHOICES)
	cover = models.ImageField(upload_to = 'page/',verbose_name = 'Cover')
	collection = models.ForeignKey(Collection, verbose_name = 'Collection', blank = True, null = True,help_text = 'Leave it to blank when the page type is not COLLECTION')

	class Meta:
		verbose_name = 'Page'
		verbose_name_plural = 'Page'

	def __unicode__(self):
		s = ''
		if self.ptype == 'collection':
			s = self.name + '--'+ self.collection.name
		else:
			s = self.name
		return s

class Section(models.Model):
	page = models.ForeignKey(Page, verbose_name = 'Page')
	stype = models.CharField(max_length = 128, verbose_name = 'Section Type',choices = SECTION_TYPE_CHOICES)
	title = models.CharField(max_length = 128, verbose_name = 'Title',blank = True, null = True)
	content = models.TextField(verbose_name = 'Content',blank = True, null = True)
	image = models.ImageField(upload_to = 'section/',blank = True, null = True)
	scol = models.CharField(max_length = 128, verbose_name = 'Section Column',choices = SECTION_COL_CHOICES)
	order = models.IntegerField(verbose_name = 'Order',help_text = 'Order the section')

	class Meta:
		verbose_name = 'Section'
		verbose_name_plural = 'Section'
		ordering = ['scol','order']

	def __unicode__(self):
		return self.scol+str(self.order)

