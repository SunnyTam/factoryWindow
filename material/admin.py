# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from material.models import Fabric, Clothing, Material

admin.site.register(Material)
admin.site.register(Fabric)
admin.site.register(Clothing)