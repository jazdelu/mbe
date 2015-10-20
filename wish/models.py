from django.db import models
from collection.models import Product
from django.contrib.auth.models import User
# Create your models here.
class Wish(models.Model):
	product = models.ForeignKey(Product, verbose_name = 'Product', related_name = 'wishes')
	user = models.ForeignKey(User, verbose_name = 'User', related_name = 'wishes')
	datetime = models.DateTimeField(auto_now_add= True)

	class Meta:
		verbose_name = 'Wish'
		verbose_name_plural = 'Wish'

	def __unicode__(self):
		return self.user.username+'---'+self.product.name