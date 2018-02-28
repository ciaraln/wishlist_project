from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import User
# Create your models here.
def index(request):
 	return render(request,'lr_templates/index.html')
def register(request):
	results = User.objects.register_validation(request.POST)
	if results[0]:
		request.session['user_id'] = results[1].id 
		print "*******You're registered buddy!*********"
		return redirect('/first_app/success')
	else:
		for error in results[1]:
			messages.error(request,error)
	return redirect('/lr_app')

def login(request):
	results = User.objects.login_validation(request.POST)
	if results[0]:
		request.session['user_id'] = results[1].id 
		print "*******You're logged buddy!*********"
		return redirect('/first_app/success')
	else:
		for error in results[1]:
			messages.error(request,error)
	return redirect('/lr_app')

def logout(request):
	print "Logged Out"
	request.session.clear()
	return redirect('/lr_app')
