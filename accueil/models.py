from django.db import models

class Communes(models.Model):
    libcom = models.CharField(max_length=50, null=False)
    information_access = models.IntegerField(null=False)
    numeric_access = models.IntegerField(null=False)
    numeric_competence = models.IntegerField(null=False)
    administrative_competence = models.IntegerField(null=False)

class Departements(models.Model):
    libdep = models.CharField(max_length=50, null=False)
    libcom = models.ForeignKey(Communes, on_delete=models.CASCADE)


class Regions(models.Model):
    libreg = models.CharField(max_length=50, null=False)
    libdep = models.ForeignKey(Departements, on_delete=models.CASCADE)
