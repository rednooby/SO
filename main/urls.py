from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from . import views

urlpatterns=[
	#초기화면 main/index/
	url(r'^index/$', views.index, name='index'),
]