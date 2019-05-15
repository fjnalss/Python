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
	paginate_by = 5

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		paginator = context.get('paginator')
		current_page = context.get('page_obj')
		is_paginated = context.get('is_paginated')
		pagination_data = self.pagination_data(paginator, current_page, is_paginated)
		context.update(pagination_data)
		return context

	def pagination_data(self,paginator, current_page, is_paginated):
		if not is_paginated:
			return {}
		left = []
		right = []
		left_has_more = False
		right_has_more = False
		first = False
		last = False
		current_page_num = current_page.number
		total_pages = paginator.num_pages
		page_range = paginator.page_range
		if current_page_num == 1:
			right = page_range[current_page_num:current_page_num + 2]
			if right[-1] < total_pages - 1:
				right_has_more = True


class DetailView(generic.DetailView):
	model = Article
	template_name = 'blog/detail.html'
	context_object_name = 'article'

	def get(self, request, *args, **kwargs):    # get 方法返回的是一个 HttpResponse 实例
		#覆写 get 方法：每当文章被访问一次，就得将文章阅读量 +1
		response = super(DetailView, self).get(request, *args, **kwargs)
		self.object.increase_views()   #只有当 get 方法被调用后，才有 self.object 属性，其值为article模型实例
		return response

	def get_context_data(self, **kwargs):
		# 除了将article传递给模板外(detailview实现)，把评论表单、文章下的评论列表传递给模板
		context = super(DetailView, self).get_context_data(**kwargs)
		form = CommentForm()
		comment_list = self.object.comment_set.all()
		context.update({'form': form, 'comment_list': comment_list})
		return context



class ArchiveView(IndexView):
	def get_queryset(self):
		return super(ArchiveView, self).get_queryset().filter(create_time__year=self.kwargs.get('year'),
			                                                  create_time__month=self.kwargs.get('month'))


class CategoryView(IndexView):
	def get_queryset(self):
		cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
		return super(CategoryView, self).get_queryset().filter(category=cate)

"""
	cate = get_object_or_404(Category, pk=pk)
	article_list = Article.objects.filter(category=cate)
	return render(request, 'blog/index.html', context={'article_list': article_list})

def detail(request, pk):
	article = get_object_or_404(Article,pk=pk)
	article.increase_views()
	form = CommentForm()
	comment_list = article.comment_set.all()
	context = {'article': article,
			   'form': form,
			   'comment_list': comment_list
			   }
	return render(request, 'blog/detail.html', context=context)


class ArchiveView(generic.ListView):
	model = Article
	template_name = 'blog/index.html'
	context_object_name = 'article_list'

	def get_queryset(self):
		return Article.objects.filter(create_time__year=year,create_time__month=month).order_by('-create_time')
"""
