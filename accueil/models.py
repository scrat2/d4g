from django.db import models

class Pays(models.Model):
    name = models.CharField(max_length=50, null=False)

class Regions(models.Model):
    name = models.CharField(max_length=50, null=False)

class Departements(models.Model):
    name = models.CharField(max_length=50, null=False)

class Communes(models.Model):
    name = models.CharField(max_length=50, null=False)
