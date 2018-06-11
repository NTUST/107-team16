
from django.db import models

from django.utils import timezone

class Contactus(models.Model):
	content = models.CharField(max_length=1000)

	def __str__(self):
		return self.content