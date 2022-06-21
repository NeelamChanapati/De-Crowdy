from django.db import models
from django.utils import timezone

# Create your models here.
class order(models.Model):
	name = models.CharField(max_length=50)
	ph_no = models.IntegerField()
	items = models.CharField(default='0', max_length=200)
	addons = models.CharField(max_length=200)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name