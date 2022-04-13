from operator import mod
from pyexpat import model
from tkinter import CASCADE
from django.db import models
# Create your models here.


class Quetions(models.Model):
    quetion = models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return self.quetion


class Answers(models.Model):
    quetion = models.ForeignKey(Quetions,on_delete=CASCADE)
    answer = models.TextField(null=True,blank=True)

    