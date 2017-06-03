# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import QueryDict
from django.db import IntegrityError
from django.contrib.auth.models import User
from . models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.views import login

# Create your views here.

def registration(request):
	
	if request.user.is_authenticated():
		return HttpResponseRedirect("/")
	
	errorMessage = ""
	
	# User clicks register button and we create a new user
	if request.method == "POST":
		
		post = QueryDict(request.body)
		
		iemail = post.get('email')
		ipassword = post.get('password')
		ifirst_name = post.get('first_name')
		ilast_name = post.get('last_name')		
		
		try:
			
			newUser = User.objects.create_user(username=iemail,
										password=ipassword,
										first_name=ifirst_name,
										last_name=ilast_name,
										email=iemail,)
		
			newUser.save()
		
			designer = Designer(user=newUser,)	
			designer.save()
			
			return HttpResponse("success")
		
		except IntegrityError as e:
			
			errorMessage = e
			print (e)
			return HttpResponse(e)
											
	return render(request, "login.html", {"errorMessage":errorMessage})