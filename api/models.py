from django.db import models


# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=35)
    userPass = models.CharField(max_length=35)


class Note(models.Model):
    userIdConnect = models.IntegerField()
    noteTitle = models.CharField(max_length=50)
    textNote = models.TextField()
    noteColor = models.CharField(max_length=25)
