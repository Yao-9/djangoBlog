from django.db import models

# Create your models here.
class Post(models.Model):
	pubDate = models.DateTimeField('date published')
	title = models.CharField(max_length=200)
	text = models.TextField()
