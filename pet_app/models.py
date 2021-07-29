from django.db import models
from django.db.models.fields.related import ForeignKey

class Group(models.Model):
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    animal = models.ForeignKey("Animal", on_delete=models.CASCADE, related_name="groups")

class Animal(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=255)

class Characterist(models.Model):
    name = models.CharField(max_length=255)
    animals = models.ManyToManyField(Animal)
    