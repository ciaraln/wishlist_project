from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from ..lr_app.models import User
# Create your models here.

class WishManager(models.Manager):
	def wish_validation(self,postData, user_id):
		errors = []
		if len(postData['item']) < 1:
			errors.append('You must fill in the item field.')
		if len(postData['item']) < 3:
			errors.append('Your item characters is too short, please try again.')
		time = datetime.now().strftime("%Y-%m-%d")
		if len(errors) > 0:
			return (False, errors)
		else:
			w = Wish.objects.create(
				item=postData['item'], 
				date_added=time, 
				added_by=User.objects.get(id=user_id)
				)
			return(True, w)


class Wish(models.Model):
		item = models.CharField(max_length=255)
		date_added = models.DateTimeField()
		added_by = models.ForeignKey(User, related_name='wish_added')
		wishers = models.ManyToManyField(User, related_name='wish_joined')

		created_at = models.DateTimeField(auto_now_add=True)
		updated_at = models.DateTimeField(auto_now=True)

		objects = WishManager()

		def __str__(self):
			return 'item: {}'.format(self.item)
