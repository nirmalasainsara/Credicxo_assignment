from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Teacher model
class Teacher(models.Model):
    tname = models.CharField( max_length=200)
    tage = models.IntegerField()
    tsubject = models.CharField( max_length=200
    )
 

# Student model
class Student(models.Model):
    sroll = models.IntegerField()
    sname = models.CharField( max_length=200)
    sfname = models.CharField( max_length=200)
    sage = models.IntegerField()
    
