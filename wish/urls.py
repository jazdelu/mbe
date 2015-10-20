from django.conf.urls import include, url
from wish import views

urlpatterns = [
	url(r'^$', views.get_wishes_by_product,name = 'add wish'),
    url(r'^add/', views.add,name = 'add wish'),
    url(r'^remove/', views.remove,name = 'remove wish'),

]
