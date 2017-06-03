# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Designer(models.Model):
	
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	# For python 2
	def __unicode__(self):
		return "%s %s" % (self.user.first_name, self.user.last_name)
	
	# Python 3 
	def __str__(self):
		return "%s %s" % (self.user.first_name, self.user.last_name)
