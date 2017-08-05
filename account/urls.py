from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from . import views

urlpatterns=[
	#초기화면 account/
	url(r'^join/$', views.join, name='join'),
	url(r'^login/$', views.login, name='login'),
]