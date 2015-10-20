from django.conf.urls import include, url
from collection import views

urlpatterns = [
    url(r'^(?P<hierarchy>.+)/', views.get_products_by_category,name = 'register'),
]
