from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.views import generic
from .models import Article, Tag, Category

class IndexView(generic.ListView):
	model = Article
	template_name = 'blog/index.html'
	context_object_name = 'article_list'

	def get_queryset(self):
		return Article.objects.all().order_by('-create_time')


class DetailView(generic.DetailView):
	model = Article
	template_name = 'blog/detail.html'
	context_object_name = 'article'


