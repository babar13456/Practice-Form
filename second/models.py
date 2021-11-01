from django.db import models

# Create your models here.

class Add_teacher(models.Model):
	name = models.CharField(max_length=120)
	age = models.IntegerField()
	religion = models.CharField(max_length=120)

	def __str__(self):
		return self.name
