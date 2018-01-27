from django.conf.urls import url
from . import views

app_name = 'alumini'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login_al', views.index1, name='index1'),
	url(r'^login_re', views.index2, name='index2'),
]
