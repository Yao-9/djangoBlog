import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	pubDate = models.DateTimeField('date published')
	title = models.CharField(max_length=200)
	text= models.TextField()

	def wasPublishedRecently(self):
		return self.pubDate >= timezone.now() - datetime.timedelta(days=1)

	def __str__(self):
		return self.title

class Catagory(models.Model):
	name = models.CharField(max_length=40)
