from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from member.models import Member
# Register your models here.

class MemberInline(admin.StackedInline):
	model = Member
	can_delete = False
	verbose_name_plural = 'member'


class UserAdmin(UserAdmin):
	list_display = ('username','email','email1', 'kidsname')
	def email1(self,obj):
		return obj.member.email1
	email1.short_description = "Friends' Email"

	def kidsname(self,obj):
		return obj.member.kidsname	
	kidsname.short_description = "Kids' Names"

	list_display = ('username','email','email1', 'kidsname')
	inlines = (MemberInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)