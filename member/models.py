from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Member(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	email1 = models.EmailField(blank = True, null = True, verbose_name = "Friend's email" )
	surname = models.CharField(max_length = 128, verbose_name = 'Surname', blank = True, null = True)
	nickname = models.CharField(max_length = 128, verbose_name = 'Nickname', blank = True, null = True )
	kidname = models.CharField(max_length = 128, verbose_name = 'Kids Name', blank = True, null = True)
	address = models.TextField(verbose_name = 'Address', blank = True, null = True)

	def __unicode__(self):
		return self.surname