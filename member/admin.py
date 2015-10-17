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
	inlines = (MemberInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)