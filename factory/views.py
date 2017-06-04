# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

#@login_required(login_url="/login/")
def request_form(request):
	
	context = {}
	return render(request, "contact.html", context)

def results(request):
	return render(request, "results.html")

	
	