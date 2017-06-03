# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Material(models.Model):
    name = models.TextField()

class Fabric(models.Model):
    material = models.OneToOneField(Material, on_delete=models.CASCADE)

class Clothing(models.Model):
    material = models.OneToOneField(Material, on_delete=models.CASCADE)