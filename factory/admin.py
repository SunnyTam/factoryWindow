# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from factory.models import Factory, Order

admin.site.register(Factory)
admin.site.register(Order)
