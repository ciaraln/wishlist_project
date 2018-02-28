# -# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

import bcrypt


class UserManager(models.Manager):
	def register_validation(self, postData):
		errors = []
		if len(postData['name']) < 3:
			errors.append('Name must be longer than 3 character')
		if len(postData['usename'] ) < 3:
			errors.append('Usename should be more than 3 characters')
		if len(postData['password']) < 8:
			errors.append('Password must be at least 8 characters long')
		if postData['password'] != postData['passwordcheck']:
			errors.append('Passwords do not match')
		if len(errors) > 0:
			return (False, errors)
		else:
			hash_pwd = bcrypt.hashpw(postData['password'].encode('utf-8'), bcrypt.gensalt())
			u = User.objects.create(name=postData['name'], usename=postData['usename'], password=hash_pwd)
			return(True, u)

	def login_validation(self,postData):
		errors = []
		if len(postData['usename'] ) < 3:
			errors.append('Usename should be more than 3 characters')
		if len(postData['password']) < 8:
			errors.append('Password must be at least 8 characters long')
		if len(errors) > 0:
			return (False, errors)
		else:
			u = User.objects.filter(usename=postData['usename'])
			if u:
				print "User found"
				if bcrypt.checkpw(postData['password'].encode('utf-8'),u[0].password.encode('utf-8')):
					u[0].password == postData['password']
					return (True, u[0])
				else:
					errors.append('Incorrect Password')
					return(False, errors)
			else:
				print 'User not found'
				errors.append('No user exists with this usename')
				return (False, errors)

class User(models.Model):
	name = models.CharField(max_length = 255)
	usename = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)

	created_at  = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

	def __str__(self): # dont forget to space 

		return 'name: {}, usename: {}'.format(self.name, self.usename)
# Create your models here.
