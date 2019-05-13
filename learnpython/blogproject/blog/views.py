from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader
from django.views import generic
from .models import Article, Tag, Category
from comments.forms import CommentForm

class IndexView(generic.ListView):
	model = Article
	template_name = 'blog/index.html'
	context_object_name = 'article_list'


"""
class DetailView(generic.DetailView):
	model = Article
	template_name = 'blog/detail.html'
	context_object_name = 'article'
"""


def detail(request, pk):
	article = get_object_or_404(Article,pk=pk)
	form = CommentForm()
	comment_list = article.comment_set.all()
	context = {'article': article,
			   'form': form,
			   'comment_list': comment_list
			   }
	return render(request, 'blog/detail.html', context=context)


def archive(request, year, month):
	article_list = Article.objects.filter(create_time__year=year,create_time__month=month)
	return render(request, 'blog/index.html', context={'article_list': article_list})


def category(request, pk):
	cate = get_object_or_404(Category, pk=pk)
	article_list = Article.objects.filter(category=cate)
	return render(request, 'blog/index.html', context={'article_list': article_list})
"""
class ArchiveView(generic.ListView):
	model = Article
	template_name = 'blog/index.html'
	context_object_name = 'article_list'

	def get_queryset(self):
		return Article.objects.filter(create_time__year=year,create_time__month=month).order_by('-create_time')
"""
