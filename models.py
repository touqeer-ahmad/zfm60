from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employee(models.Model):
    slot = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    timestamp = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    dpt = models.CharField(max_length=30)
    ost = models.CharField(max_length=30)
    oet = models.CharField(max_length=30)
    def __unicode__(self):
        return self.fname

class Employeeinfo(models.Model):
    slot = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    timestamp = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    dpt = models.CharField(max_length=30)
    ost = models.CharField(max_length=30)
    oet = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    def __unicode__(self):
        return self.timestamp

class enroll(models.Model):
    event = models.CharField(max_length=50)
