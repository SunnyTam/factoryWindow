# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from users.models import *
# Create your models here.

class Factory(models.Model):
	name = models.TextField()
	user = models.OneToOneField(User, on_delete=models.CASCADE)

MAYBECHOICE = (
    ('p', 'Pending'),
    ('a', 'Accepted'),
    ('r', 'Rejected'),
)
	
class Order(models.Model):
	
	status = models.CharField(max_length=1, choices=MAYBECHOICE)
	requestDesigner = models.ForeignKey(Designer)
	targetManufacturer = models.ForeignKey(Factory)