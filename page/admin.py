from django.contrib import admin
from page.models import Section, Page

# Register your models here.
class SectionAdmin(admin.ModelAdmin):
	list_filter = ('page','stype','scol')
	list_display = ('position','stype','scol','order','page')
	fields = ('stype','scol','order','page','title','content','image')

	def position(self,obj):
		return obj.scol+str(obj.order)

admin.site.register(Section,SectionAdmin)

admin.site.register(Page)
