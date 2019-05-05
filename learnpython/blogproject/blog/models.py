from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	create_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	page_views = models.IntegerField(default=0)
	comment = models.TextField()
	category = models.ForeiginKey(Category)
	tags = models.ForeiginKey(Tag, blank=True)
	author = models.ForeiginKey(User)


class 
