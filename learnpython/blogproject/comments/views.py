from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Comment
from .forms import CommentForm


def article_comment(request, article_pk):
	article = get_object_or_404(Article, pk=article_pk)
	if request.method == 'POST':
		form = CommentForm(request.POST)  #用户提交的数据存在 request.POST 中，这是一个类字典对象
		if form.is_valid():   #Django 自动帮我们检查表单的数据是否符合格式要求
			comment = form.save(commit=False)  #调用表单的save方法保存数据到数据库,commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库
			comment.article = article 
			comment.save()  #将评论数据保存进数据库，调用模型实例的 save 方法
			return HttpResponseRedirect(reverse('blog:detail', args=(article.id,)))
		else:
			comment_list = article.comment_set.all()  #使用 post.comment_set.all() 反向查询全部评论
			context = {'article': article,
					   'form': form,
					   'comment_list': comment_list
					   }
			return render(request, 'blog/detail.html', context=context)
	return HttpResponseRedirect(reverse('blog:detail', args=(article.id,)))
