from django.shortcuts import render
from django.conf import settings
# Create your views here.

#회원가입 페이지.	account/join/
def join(requst):
	return render(requst, 'account/join.html')

#로그인 페이지.		account/login/
def login(requst):
	return render(requst, 'account/login.html')