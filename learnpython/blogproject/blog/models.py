from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
	"""文章的标签"""
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Category(models.Model):
	"""文章的分类"""
	name = models.CharField(max_length=100, default='其他')

	def __str__(self):
		return self.name


class Article(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	create_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	page_views = models.IntegerField(default=0)
	comment = models.TextField(blank=True)
	category = models.ForeignKey(Category, default='其他', on_delete=models.SET_DEFAULT)
	tags = models.ManyToManyField(Tag, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title




		