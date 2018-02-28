from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..lr_app.models import User
from models import Wish
from django.contrib import messages

def success(request):
	user = User.objects.get(id=request.session['user_id'])
	print user.name
	context = {
		"name" : user.name, 
		"my_items" : Wish.objects.filter(added_by=request.session['user_id']),
		"all_items" : Wish.objects.exclude(added_by=request.session['user_id']).exclude(wishers=request.session['user_id']),
		"my_adds" : Wish.objects.filter(wishers=request.session['user_id']),
	}
	return render(request,'first_templates/home.html', context)

def additem(request):
	return render(request, 'first_templates/additem.html')

def saveitem(request):
	results = Wish.objects.wish_validation(request.POST, request.session['user_id'])
	if results[0]:
		request.session['wish_id'] = results[1].id
		print "*****Your Item was added, YEAH!!!*******"
		return redirect('/first_app/success')
	else:
		for error in results[1]:
			messages.error(request,error)
		return redirect('/first_app/success')
	return redirect('first_templates/home.html')

def add_wish(request, wish_id):
	w = Wish.objects.get(id=wish_id)
	u = User.objects.get(id=request.session['user_id'])

	w.wishers.add(u)
	print w.wishers.all()
	return redirect('/first_app/success')

def item(request, wish_id):
	results = Wish.objects.get(id=wish_id)

	context = {
		"this_item" : results, 
		"item_wishers" : results.wishers.all()
		}
	print "We are viewing items!"
	print results.item
	return render(request, 'first_templates/item.html', context)

def remove(request, wish_id):
	w = Wish.objects.get(id=wish_id)
	u = User.objects.get(id=request.session['user_id'])

	w.wishers.remove(u)
	print w.wishers.all()
	return redirect('/first_app/success')

def delete(request, wish_id):
	Wish.objects.get(id=wish_id).delete()
	return redirect('/first_app/success')

# the missing piece
def displayothers(request):
	list_item = Wish.objects.get(id=wish_id)
	people_interested= User.objects.filter(items_wanted=wish_id)
	context =  {
		'item' : list_item.item,
		'people_interested' : people_interested,
	}
	return render(request, 'first_templates/item.html', context)

# Create your views here.
