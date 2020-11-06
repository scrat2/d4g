from django.db import models


class Regions(models.Model):
    numreg = models.IntegerField(primary_key=True)
    libreg = models.CharField(max_length=50, null=False)
    global_score = models.IntegerField(null=False)
    numeric_access = models.IntegerField(null=False)
    information_access = models.IntegerField(null=False)
    numeric_competence = models.IntegerField(null=False)
    administrative_competence = models.IntegerField(null=False)


class Departements(models.Model):
    numreg = models.ForeignKey(Regions, to_field='numreg', on_delete=models.CASCADE)
    libdep = models.CharField(max_length=50, null=False)
    numdep = models.CharField(primary_key=True, max_length=4)
    global_score = models.IntegerField(null=False)
    administrative_competence = models.IntegerField(null=False)
    numeric_competence = models.IntegerField(null=False)
    information_access = models.IntegerField(null=False)
    numeric_access = models.IntegerField(null=False)


class Communes(models.Model):
    libcom = models.CharField(max_length=50, null=False)
    code_postal = models.CharField(max_length=7, null=False)
    global_score = models.IntegerField(null=False)
    information_access = models.IntegerField(null=True)
    numeric_access = models.IntegerField(null=True)
    numeric_competence = models.IntegerField(null=True)
    administrative_competence = models.IntegerField(null=True)
    numdep = models.ForeignKey(Departements, to_field='numdep', on_delete=models.CASCADE)
